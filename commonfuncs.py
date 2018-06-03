#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/3/26
# @Author : 茶葫芦
# @Site   : 
# @File   : commonfuncs.py

from tornado.web import RequestHandler
import uuid

def check_session(RequestHandler_obj):
    """检测session是否有效,没有则session cookie"""
    sessionid=RequestHandler_obj.get_secure_cookie("sessionid")
    RequestHandler_obj.session =None
    if sessionid:
        sess_data=RequestHandler_obj.db.get("select session_data from h_session where sessionid = %(sessionid)s",sessionid=sessionid)
        RequestHandler_obj.session=sess_data


