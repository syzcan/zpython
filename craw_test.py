#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
reload(sys) 
sys.setdefaultencoding('utf8') 
import craw_job
import craw_pyquery

#存储表
craw_store = "craw"
craw_url = "https://segmentfault.com/t/java?type=newest&page=1"
craw_item = '.stream-list__item'
# 下一页规则有两种，1:css选择器 2:【url】根据当前地址正则解析下一页，页数+1
# craw_next = craw_pyquery.craw_rule("craw_next",".pagination>.next>a","attr","href")
craw_next = craw_pyquery.craw_rule("craw_next","","url[page=(\d+)]","")
# 扩展字段解析规则
url_rule = craw_pyquery.craw_rule("url","h2.title a","attr","href")
title_rule = craw_pyquery.craw_rule("title","h2.title","text","")
extFields = [url_rule,title_rule]	

# craw_job.craw_list(craw_url,craw_item,craw_next,craw_store,extFields)
# craw_job.craw_detail(craw_url,craw_store,extFields)
# url_rule = craw_pyquery.craw_rule("url",".stream-list__item h2.title a","attr[/q(.*)]","href","array")
# data = craw_pyquery.craw_detail(craw_url,[url_rule]) 

# 控制台回车解析下一页
while True:
	cmd = raw_input("Enter craw nextpage [exit to quit]:")
	if cmd == '':
		datas,craw_url = craw_pyquery.craw_list(craw_url,craw_item,craw_next,extFields)
		count = 1
		for data in datas:
			print count,data['title']+"\n"+data['url']
			count += 1
	elif cmd == 'exit':	
		break
	else:
		print 'error cmd:'+cmd		