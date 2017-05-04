#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
reload(sys) 
sys.setdefaultencoding('utf8') 
import craw_pyquery
from common_dao import insert as insert

craw_url = "http://www.runoob.com/"
craw_item = '.codelist-desktop a.item-top'

url_rule = craw_pyquery.craw_rule("url","a","attr","href")
title_rule = craw_pyquery.craw_rule("title","h4","text","")
icon_rule = craw_pyquery.craw_rule("icon","img","attr","src")
extFields = [url_rule,title_rule,icon_rule]


for data in craw_pyquery.craw_list(craw_url,craw_item,extFields):
	insert("craw",{"url":data['url'],"title":data['title']})
	print "insert: ",data['url']