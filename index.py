#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/3/25
# @Author : 茶葫芦
# @Site   : 
# @File   : index.py

import json
from BaseHandler import BaseHandler
import tornado
import time
import uuid
from response_code import RET
import hashlib
from tornado.web import RequestHandler
import json



class pageindexhdl(BaseHandler):#欢迎页面
    def get(self):
        self.render('index.html')

class pageloginhdl(BaseHandler):#登陆页面
    def get(self):
        #进入登陆界面,原先cookie作废,要求输入用户密码进入
        user_no=self.get_cookie("user_no_cookie","ADMI")
        # self.clear_cookie("sessionid")
        return self.render('login.html',user_no=user_no)


class pagebilllisthdl(BaseHandler):#销售单列表|添加|查看|修改
    def get(self):
        part_no=self.get_query_argument("part_no","",True)
        zhifu=self.get_query_argument("zhifu","",True)
        stock_out=self.get_query_argument("stock_out","",True)
        wherestr=""
        if part_no:
            wherestr=" part_no = '"+part_no+"'"
        if zhifu:
            if wherestr:
                wherestr=wherestr+ " and "+" is_pay = '"+zhifu+"'"
            else:
                wherestr=" is_pay = '"+zhifu+"'"
        if stock_out:
            if wherestr:
                wherestr=wherestr+ " and "+" stock_out = '"+stock_out+"'"
            else:
                wherestr=" stock_out = '"+stock_out+"'"
        if wherestr:
            wherestr=" where "+wherestr
        # print "wherestr:"+wherestr
        try:
            querystr="select bill_id,part_no,bill_price,bill_qty,cust_name,cust_tel,cust_email,bill_date,is_pay,stock_out,bill_person from h_bill"+wherestr
            rows=self.db.query(querystr)
        except Exception as e:
            self.write("%s",e)
        self.render("billList.html",session=self.session,rows=rows,part_no=part_no,zhifu=zhifu,stock_out=stock_out)
class pagebilladdhdl(BaseHandler):
    def get(self):
        self.render("billadd.html", session=self.session)
class pagebillviewhdl(BaseHandler):
    def get(self):
        bill_id=self.get_query_argument("bill_id","",True)
        row=self.db.get("select bill_id,part_no,bill_price,bill_qty,cust_name,cust_tel,cust_email,bill_date,is_pay,stock_out,bill_person from h_bill where bill_id = %(bill_id)s" ,bill_id=bill_id)
        self.render("billView.html", session=self.session,row=row)
class pagebillupdatehdl(BaseHandler):
    def get(self):
        bill_id = self.get_query_argument("bill_id", "", True)
        row = self.db.get(
            "select bill_id,part_no,bill_price,bill_qty,cust_name,cust_tel,cust_email,bill_date,is_pay,stock_out,bill_person from h_bill where bill_id = %(bill_id)s",
            bill_id=bill_id)
        self.render("billUpdate.html", session=self.session,row=row)




