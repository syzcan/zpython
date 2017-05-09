#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf8') 
import time
from zlibs import craw_util
from zlibs import common_dao

def craw_list(craw_url,craw_item,craw_next,craw_store,extFields,headers=None,cookies=None):
	datas,craw_next = craw_util.craw_list(craw_url,craw_item,craw_next,extFields)

	for data in datas:
		save_data(craw_store,data)
	return (datas,craw_next)

def craw_detail(craw_url,craw_store,extFields,headers=None,cookies=None):
	data = craw_util.craw_detail(craw_url,extFields)
	save_data(craw_store,data)	

def save_data(craw_store,data):
	for key in data.keys():
		# list类型转为字符串,拼接，不然不能插入数据库
		if isinstance(data[key],list):
			val = "["
			val += ",".join(data[key])
			val += "]"
			data[key] = val
	try:
		common_dao.insert(craw_store,data)
	except Exception, e:
		print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"craw error:",e
	else:
		print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"craw success:",data