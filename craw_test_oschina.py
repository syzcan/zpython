#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
reload(sys) 
sys.setdefaultencoding('utf8') 
import craw_job
from craw_pyquery import craw_rule

craw_store = "craw_store"
craw_url = "https://www.oschina.net/project/zh?p=1"
craw_item = '.news-list a.item'
craw_next = craw_rule("craw_next","","url[p=(\d+)]","")

url_rule = craw_rule("url","a","attr","href")
title_rule = craw_rule("title",".title","text","")
summary_rule = craw_rule("summary",".summary","text","")
extFields = [url_rule,title_rule,summary_rule]	

# 回车开始抓取craw_url，或者输入指定craw_url再抓取
cmd = raw_input("Enter craw ["+craw_url+"] or input craw_url:")
if cmd !='':
	craw_url = cmd
print "=====craw start=====\n"
while True:
	if craw_url != '':
		print "now start craw",craw_url,"\n"
		datas,craw_url = craw_job.craw_list(craw_url,craw_item,craw_next,craw_store,extFields)
		if len(datas) == 0:
			print "there is no data\n"
			print "=====craw end====="
			break
	else:
		print "there is no next page\n"
		print "=====craw end====="
		break
		