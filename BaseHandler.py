#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/3/26
# @Author : 茶葫芦
# @Site   : 
# @File   : BaseHandler.py

from tornado.web import RequestHandler
import json
import torndb
import uuid

class BaseHandler(RequestHandler):

    """封装RequesetHandler基类,通用方法自动调用"""

    @property
    def db(self):
        """作为RequestHandler对象的db属性"""
        return self.application.db

    @property
    def redis(self):
        return self.application.redis

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict={}

    #
    # # def set_default_headers(self):
    # #     self.set_header("Content-Type", "application/json; charset=UTF-8")
    #
    # def check_session(self):
    #     """
    #     sessionid规则:user_no+password+混淆字符串进行sha2操作
    #     sessionid判定合法原则:
    #     登陆界面:是如果有sessionid直接清除,登陆成功后重新置sessionid
    #     其他界面:有sessionid即可.否则返回登陆界面
    #     sessionid 对应的cookie设置成关闭浏览器就失效,退出系统也手动设置成失效.
    #     """
    #
    #     self.sessionid = self.get_secure_cookie("sessionid")
    #     self.session = None
    #     if self.sessionid:
    #         sess_data = self.db.get("select session_data from h_session where sessionid = %(sessionid)s",
    #                                 sessionid=self.sessionid)
    #
    #         self.session = eval(dict(sess_data).get("session_data",''))
    #
    #     else: #如果sessionid不存在,直接跳转登陆界面
    #         return self.redirect("/login")


    def dbget(self, getString):
        """数据库读取封装,若出错直接返回错误对象 """
        try:
            db_ret = self.db.get(getString)
        except Exception as e:
            return e
        return db_ret

    def dbquery(self, queryString):
        try:
            db_ret = self.db.query(queryString)
        except Exception as e:
            return e
        return db_ret
