#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/6/4
# @Author : 茶葫芦
# @Site   : 
# @File   : Spider.py

import requests
from USER_AGENT import USER_AGENT_LIST
import random
from lxml import etree
import torndb
import config
import time
import redis

"""爬虫"""


class newsSpider():
    def __init__(self):
        """
        连接mysql数据库和redis数据库
        """
        self.db = torndb.Connection(**config.mysqlconf)
        try:
            self.redis = redis.StrictRedis(**config.redisconf)
        except Exception, e:
            print e.message
        self.header = {"User-Agent": random.choice(USER_AGENT_LIST)}

    def getSinaNewsSourceUrls(self):  # 新浪
        """
        1.拿到首页,取得指定模块的新闻链接4
        2.打开新闻链接,爬取内容(已经爬过的网页不再爬取)
        3.爬取的内容入库,爬取过的网页入库
        """
        source_url = "http://news.sina.com.cn/"
        mainPage = requests.get(source_url, headers=self.header)
        # print(mainPage.content)
        htmltext = etree.HTML(mainPage.content)

        urls = set()
        news1 = htmltext.xpath('//*[@id="syncad_1"]/*/a')
        for c in news1:
            url = c.xpath('./@href')[0]
            urls.add(url)  # 如果没有爬取过加入前台待爬集合
        news2 = htmltext.xpath('//*[@id="ad_entry_b2"]/ul/li/a')
        for c in news2:
            url = c.xpath('./@href')[0]
            urls.add(url)
        news3 = htmltext.xpath('// *[ @ id = "blk_sh_011"]/li/a')
        for c in news3:
            url = c.xpath('./@href')[0]
            urls.add(url)
        news4 = htmltext.xpath('// *[ @ id = "blk_ndxw_01"] / ul/li/a')
        for c in news4:
            url = c.xpath('./@href')[0]
            urls.add(url)

        self.redis.sadd('new_urls', *list(urls))  # 整体入redis后台数据库
        self.redis.sdiffstore('new_urls', 'new_urls', 'loaded_urls')  # 将新链接和已爬链接交集,得到没爬过的链接集合
        self.redis.sunionstore("preload_urls", 'new_urls', 'preload_urls')  # 没爬过的加入待爬集合
        self.redis.delete('new_urls')  # 删除新链接集合
        return "over"

    def spider_run(self):
        news_content = []
        while True:
            time.sleep(1+random.random())
            url = self.redis.spop('preload_urls')
            if url:
                resp = requests.get(url=url, headers=self.header)
                htmltext = etree.HTML(resp.content)
                try:
                    title = htmltext.xpath('//h1[@class="main-title"]')[0].text  # 标题
                except Exception as e:
                    self.redis.sadd('runerror_urls',url)   #爬取错误的列表进行收集,分析原因
                    continue
                try:
                    pubdatetime = htmltext.xpath('//div[@class="date-source"]/span[@class="date"]')[0].text.replace(u'年','-').replace(u'月', '-').replace(u'日', '')  # 日期
                except Exception as e:
                    self.redis.sadd('runerror_urls', url)
                    continue
                print(pubdatetime)
                try:
                    source = htmltext.xpath('//div[@class="date-source"]/a[@class="source"]')[0].text  # 来源
                except Exception as e:
                    self.redis.sadd('runerror_urls', url)
                    continue
                try:
                    article = etree.tostring(htmltext.xpath('//*[@id="article"]')[0], method='html',
                                             encoding='utf-8')  # 正文html(带标签)

                except Exception as e:
                    self.redis.sadd('runerror_urls', url)
                    continue
                print((url, title, pubdatetime, source))
                news_content.append((url, title, pubdatetime, source, article))
                self.redis.sadd('loaded_urls', url)  # 添加入已爬列表
            else:
                break
        sqlstr = 'insert into t_news(url_link,news_title,news_date,news_source,news_text)values(%s,%s,%s,%s,%s)'
        self.db.executemany(sqlstr, news_content)
        return "over"


if __name__ == '__main__':
    spider = newsSpider()
    print spider.getSinaNewsSourceUrls()
    print spider.spider_run()

