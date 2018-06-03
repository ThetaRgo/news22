#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/3/26
# @Author : 茶葫芦
# @Site   : 
# @File   : Session.py

import json
import uuid


class session(object):
    def __init__(self,RequestHandler_obj):
        self.sessionid =RequestHandler_obj.get_secure_cookie('sessionid')
        if self.sessionid:
            self.data=RequestHandler_obj.dbget("select session_data from h_session where sessionid = {0}".format(self.sessionid))
        else:
            self.sessionid = uuid.uuid4().hex
            self.data = {}
            RequestHandler_obj.set_secure_cookie("sessionid", self.sessionid)