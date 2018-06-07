#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/6/4
# @Author : 茶葫芦
# @Site   : 
# @File   : sinaSpider.py

import requests
from USER_AGENT import USER_AGENT_LIST
import random
from lxml import etree
import torndb
import config
import time
import redis

"""新浪爬虫"""
class newsSpider():

    def __init__(self):
        #连接mysql数据库和redis数据库
        self.db = torndb.Connection(**config.mysqlconf)
        try:
            self.redis = redis.StrictRedis(**config.redisconf)
        except Exception, e:
            print e.message
        self.header={"User-Agent":random.choice(USER_AGENT_LIST)}
    #新浪
    def getSinaNewsSourceUrls(self):
        """
        1.拿到首页,取得指定模块的新闻链接4
        2.打开新闻链接,爬取内容(已经爬过的网页不再爬取)
        3.爬取的内容入库,爬取过的网页入库
        """
        source_url="http://news.sina.com.cn/"
        mainPage=requests.get(source_url,headers=self.header)
        print(mainPage.content)
        htmltext = etree.HTML(mainPage.content)
        #爬取4段
        urls=set()
        news1=htmltext.xpath('//*[@id="syncad_1"]/*/a')
        for c in news1:
            url,url_title=c.xpath('./@href')[0],c.text
            #如果没有爬取过加入前台待爬集合
            urls.add(url)
        news2=htmltext.xpath('//*[@id="ad_entry_b2"]/ul/li/a')
        for c in news2:
            url, url_title = c.xpath('./@href')[0],c.text
            urls.add(url)
        news3 = htmltext.xpath('// *[ @ id = "blk_sh_011"]/li/a')
        for c in news3:
            url, url_title = c.xpath('./@href')[0], c.text
            urls.add(url)
        news4 = htmltext.xpath('// *[ @ id = "blk_ndxw_01"] / ul/li/a')
        for c in news4:
            url, url_title = c.xpath('./@href')[0], c.text
            urls.add(url)
        #整体入redis后台数据库
        self.redis.sadd('new_urls',*list(urls))
        #将新链接和已爬链接交集,得到没爬过的链接集合
        self.redis.sdiffstore('new_urls','new_urls','loaded_urls')
        #没爬过的加入待爬集合
        self.redis.sunionstore("preload_urls",'new_urls','preload_urls')
        #删除新链接集合
        self.redis.delete('new_urls')
        return 0

    def spider_run(self):
        news_content=[]
        while True:
            url=self.redis.spop('loaded_urls')
            if url:
                self.redis.sadd('loaded_urls',url) #添加入已爬列表
                resp=requests.get(url=url,headers=self.header)
                htmltext = etree.HTML(resp.content)
                title, datetime, source, article="","","",""
                # title=htmltext.xpath('//*[@class="main-title"]')[0].text      #标题 /html/body/div[3]/h1
                # datetime=htmltext.xpath('//*[@class="date-source"]/[@class="date"]').text #日期
                # source=htmltext.xpath('//*[@class="date-source"]/[@class="source"]').text #来源
                # article=htmltext.xpath('// *[ @ id = "article"]').text #正文
                print((url,title))
                news_content.append((url,title,datetime,source,article))
            else:
                break
        sqlstr = 'insert into t_news(url_link,news_title,news_date,news_source,news_text)values(%s,%s,%s,%s,%s)'
        self.db.executemany(sqlstr, news_content)
        return 0


if __name__ == '__main__':
    spider=newsSpider()
    #print spider.getSinaNewsSourceUrls()
    print spider.spider_run()
    # resp = requests.get(url='http://news.sina.com.cn/c/2018-06-07/doc-ihcscwwz9446235.shtml', headers={"User-Agent":random.choice(USER_AGENT_LIST)})
    # print(resp.content)
    # val=[(1,2,3,4),(4,5,6,7),(7,8,9,10)]
    # db = torndb.Connection(**config.mysqlconf)
    # sqlstr='insert into t_news(url_link,news_title,news_source,news_text)values(%s,%s,%s,%s)'
    # db.executemany(sqlstr,val)


