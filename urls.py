#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/3/26
# @Author : 茶葫芦
# @Site   : 
# @File   : urls.py

import index
from tornado.options import define, options
import os
from tornado.web import StaticFileHandler

define('port', 9110, type=int, help="服务器运行端口")

rute_urls = [(r'/index', index.pageindexhdl),  # 系统主界面
             (r'/(\d+)',index.newshdl) #新闻页面

             ]
