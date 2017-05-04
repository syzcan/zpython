#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
reload(sys) 
sys.setdefaultencoding('utf8') 
import requests
from pyquery import PyQuery as pq

'''
解析列表页面
'''
def craw_list(craw_url,craw_item,extFields):
	response = requests.get(craw_url)
	content = response.text
	doc = pq(content)
 	
 	items = doc(craw_item).items()
 	datas = []
 	for item in items:
 		data = parse_ext(craw_url,item,extFields)
 		datas.append(data)	
 	return datas

'''
解析详情页面
'''
def craw_detail(craw_url,extFields):
	response = requests.get(craw_url)
	content = response.text
	doc = pq(content)
 		
 	return parse_ext(craw_url,doc,extFields) 	

'''
解析扩展字段
'''
def parse_ext(craw_url,item,extFields):
 	data = {}
	for ext in extFields:
		key = ext['rule_ext_name']
		val = ''
		items = item(ext['rule_ext_css'])
		if items.length > 0:
			if ext['rule_ext_type'] == 'text':
				if ext['rule_ext_mode'] == 'array':
					val = []
	 				for i in range(0,items.length):
	 					val.append(items.eq(i).text())
				else:	
					val = items.eq(0).text()
			elif ext['rule_ext_type'] == 'html':
				if ext['rule_ext_mode'] == 'array':
					val = []
	 				for i in range(0,items.length):
	 					val.append(items.eq(i).html())
				else:	
					val = items.eq(0).html()
	 		elif ext['rule_ext_type'] == 'attr':
	 			if ext['rule_ext_mode'] == 'array':
	 				val = []
	 				for i in range(0,items.length):
	 					v = items.eq(i).attr(ext['rule_ext_attr'])
	 					if ext['rule_ext_attr'] == 'href' or ext['rule_ext_attr'] == 'src':
	 						v = deal_link(craw_url,v)	
	 					val.append(v)
				else:	
					val = items.eq(0).attr(ext['rule_ext_attr'])
	 				if ext['rule_ext_attr'] == 'href' or ext['rule_ext_attr'] == 'src':
	 					val = deal_link(craw_url,val)	
 		data[key] = val
 	return data		

'''
src和href等链接判断是否加http和项目路径
'''
def deal_link(craw_url,link):
	protocal = craw_url.split("://")[0]
	domain = craw_url.split("://")[0] + "://" + craw_url.split("://")[1].split("/")[0]
	if link.startswith("//"):
		link = protocal + ":" + link;
	elif not link.startswith("http") and ""!=link:
		if link.startswith("/"):
			link = domain + link
		else:
			link = domain + "/" + link
	return link

'''
封装抓取规则
'''
def craw_rule(rule_ext_name,rule_ext_css,rule_ext_type,rule_ext_attr,rule_ext_mode="string"):
	rule = {"rule_ext_name":rule_ext_name,"rule_ext_css":rule_ext_css,"rule_ext_type":rule_ext_type,"rule_ext_attr":rule_ext_attr,"rule_ext_mode":rule_ext_mode}
	return rule
 