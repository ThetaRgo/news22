#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/3/26
# @Author : 茶葫芦
# @Site   : 
# @File   : config.py

import os

# application配置参数
settings = dict(
    static_path=os.path.join(os.path.dirname('__file__'), 'static'),
    template_path=os.path.join(os.path.dirname('__file__'), 'static'),
    debug=True,
    cookie_secret="2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=",
)

mysqlconf = dict(
    host='127.0.0.1',
    user='root',
    password='',
    database='news'
)

redisconf = dict(
    host='119.23.66.55',
    port=6379,
    db=9,
    password='1Q2W3E'

)
