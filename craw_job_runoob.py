#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
reload(sys) 
sys.setdefaultencoding('utf8') 
import craw_pyquery
import common_dao

def craw_list(craw_url,craw_item,extFields):
	for data in craw_pyquery.craw_list(craw_url,craw_item,extFields):
		for key in data.keys():
		# list类型转为字符串,拼接，不然不能插入数据库
		if isinstance(data[key],list):
			val = "["
			val += ",".join(data[key])
			val += "]"
			data[key] = val
		common_dao.insert(craw_store,data)
		print "craw:",data

def craw_detail(craw_url,extFields):
	data = craw_pyquery.craw_detail(craw_url,extFields)
	for key in data.keys():
		# list类型转为字符串,拼接，不然不能插入数据库
		if isinstance(data[key],list):
			val = "["
			val += ",".join(data[key])
			val += "]"
			data[key] = val
	common_dao.insert(craw_store,data)
	print "craw:",data		

#存储表
craw_store = "craw"

craw_url = "http://www.runoob.com/"
craw_item = '.codelist-desktop a.item-top'

url_rule = craw_pyquery.craw_rule("url","a","attr","href","array")
title_rule = craw_pyquery.craw_rule("title","h4","text","","array")
extFields = [url_rule,title_rule]	

# craw_list(craw_url,craw_item,extFields)
craw_detail(craw_url,extFields)