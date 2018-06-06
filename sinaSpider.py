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
    """
    1.拿到首页,取得指定模块的新闻链接4
    2.打开新闻链接,爬取内容(已经爬过的网页不再爬取)
    3.爬取的内容入库,爬取过的网页入库
    """
    #新浪
    def getSinaNews(self):
        source_url="http://news.sina.com.cn/"
        mainPage=requests.get(source_url,headers={"User-Agent":random.choice(USER_AGENT_LIST)})
        htmltext = etree.HTML(mainPage.content)
        #连接mysql数据库和redis数据库
        self.db = torndb.Connection(**config.mysqlconf)
        try:
            self.redis = redis.StrictRedis(**config.redisconf)
        except Exception, e:
            print e.message
        #爬取4段
        urls=set()
        news1=htmltext.xpath('//*[@id="syncad_1"]/*/a')
        for c in news1:
            url,url_title=c.xpath('./@href')[0],c.text
            #存入mysql数据库
            self.db.execute("insert into t_url (get_url_date,url_link,url_title,is_run,website_from) values (%s,%s,%s,                          %s,%s)",time.strftime('%Y-%m-%d', time.localtime(time.time())), url, url_title, 'N', source_url)
            #如果没有爬取过加入待爬集合
            if self.redis.sismember('loadurls',url):
                urls.add(url)
        news2=htmltext.xpath('//*[@id="ad_entry_b2"]/ul/li/a')
        for c in news2:
            url, url_title = c.xpath('./@href')[0],c.text
            self.db.execute("insert into t_url (get_url_date,url_link,url_title,is_run,website_from) values (%s,%s,%s,                          %s,%s)",time.strftime('%Y-%m-%d', time.localtime(time.time())), url, url_title, 'N', source_url)
            if self.redis.sismember('loadurls',url):
                urls.add(url)
        news3 = htmltext.xpath('// *[ @ id = "blk_sh_011"]/li/a')
        for c in news3:
            url, url_title = c.xpath('./@href')[0], c.text
            self.db.execute("insert into t_url (get_url_date,url_link,url_title,is_run,website_from) values (%s,%s,%s,                          %s,%s)",time.strftime('%Y-%m-%d', time.localtime(time.time())), url, url_title, 'N', source_url)
            if self.redis.sismember('loadurls',url):
                urls.add(url)
        news4 = htmltext.xpath('// *[ @ id = "blk_ndxw_01"] / ul/li/a')
        for c in news4:
            url, url_title = c.xpath('./@href')[0], c.text
            self.db.execute("insert into t_url (get_url_date,url_link,url_title,is_run,website_from) values (%s,%s,%s,                          %s,%s)",time.strftime('%Y-%m-%d', time.localtime(time.time())), url, url_title, 'N', source_url)
            if self.redis.sismember('loadurls',url):
                urls.add(url)
        #整体入库
        self.redis.sadd('newurls',urls)


        #需要尝试下数据库中直接集合差并操作是不是更好
        #mysql可以一次性全部插入.

        return 0



if __name__ == '__main__':
    spider=newsSpider()
    print spider.getSinaNews()
