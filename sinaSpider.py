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
        #连接数据库
        self.db = torndb.Connection(**config.mysqlconf)
        #爬取4段
        news1=htmltext.xpath('//*[@id="syncad_1"]/*/a')
        for c in news1:
            url,url_title=c.xpath('./@href')[0],c.text
            self.db.execute("insert into t_url (get_url_date,url_link,url_title,is_run,website_from) values (%s,%s,%s,                          %s,%s)",time.strftime('%Y-%m-%d', time.localtime(time.time())), url, url_title, 'N', source_url)

        news2=htmltext.xpath('//*[@id="ad_entry_b2"]/ul/li/a')
        for c in news2:
            url, url_title = c.xpath('./@href')[0],c.text
            self.db.execute("insert into t_url (get_url_date,url_link,url_title,is_run,website_from) values (%s,%s,%s,                          %s,%s)",time.strftime('%Y-%m-%d', time.localtime(time.time())), url, url_title, 'N', source_url)

        news3 = htmltext.xpath('// *[ @ id = "blk_sh_011"]/li/a')
        for c in news3:
            url, url_title = c.xpath('./@href')[0], c.text
            self.db.execute("insert into t_url (get_url_date,url_link,url_title,is_run,website_from) values (%s,%s,%s,                          %s,%s)",time.strftime('%Y-%m-%d', time.localtime(time.time())), url, url_title, 'N', source_url)

        news4 = htmltext.xpath('// *[ @ id = "blk_ndxw_01"] / ul/li/a')
        for c in news4:
            url, url_title = c.xpath('./@href')[0], c.text
            self.db.execute("insert into t_url (get_url_date,url_link,url_title,is_run,website_from) values (%s,%s,%s,                          %s,%s)",time.strftime('%Y-%m-%d', time.localtime(time.time())), url, url_title, 'N', source_url)




        return 0



if __name__ == '__main__':
    spider=newsSpider()
    print spider.getSinaNews()
