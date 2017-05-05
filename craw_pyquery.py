#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
reload(sys) 
sys.setdefaultencoding('utf8') 
import re
import requests
from pyquery import PyQuery as pq

'''
解析列表页面
'''
def craw_list(craw_url,craw_item,craw_next,extFields):
	response = requests.get(craw_url)
	content = response.text
	doc = pq(content)
 	
 	items = doc(craw_item).items()
 	datas = []
 	for item in items:
 		data = parse_ext(craw_url,item,extFields)
 		datas.append(data)	
 	# 下一页链接
 	next_url = ''
 	if craw_next !=None and craw_next != "":
 		if craw_next['rule_ext_type'].startswith('url'):
 			rule_ext_reg = ''
 			m = re.compile('\[(.*)\]').search(craw_next['rule_ext_type'])
 			if m:
 				rule_ext_reg = m.group(1)
 			if rule_ext_reg != '':
 				m = re.compile(rule_ext_reg).search(craw_url)
 				if m:
 					page_cont = m.group(0)
 					next_page = str(int(m.group(1)) + 1)
 					next_url = craw_url.replace(page_cont,re.sub(m.group(1),next_page,page_cont))
 		else:
 			next_url = parse_ext(craw_url,doc,[craw_next])['craw_next']
 	return (datas,next_url)

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
			rule_ext_type = ext['rule_ext_type']
			rule_ext_reg = ''
 			m = re.compile('\[(.*)\]').search(rule_ext_type)
			if m:
				rule_ext_type = rule_ext_type.replace(m.group(0),'')
				rule_ext_reg = m.group(1)

			if rule_ext_type == 'text':
				if ext['rule_ext_mode'] == 'array':
					val = []
	 				for i in range(0,items.length):
	 					val.append(items.eq(i).text())
				else:	
					val = items.eq(0).text()
			elif rule_ext_type == 'html':
				if ext['rule_ext_mode'] == 'array':
					val = []
	 				for i in range(0,items.length):
	 					val.append(items.eq(i).html())
				else:	
					val = items.eq(0).html()
	 		elif rule_ext_type == 'attr':
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
	 		# 提取内容正则进一步过滤，筛选最后一个匹配子组
	 		if rule_ext_reg != '':
	 			if isinstance(val,list):
	 				val_list = []
	 				for v in val:
	 					m = re.compile(rule_ext_reg).search(v)			
			 			if m:
			 				val_list.append(m.group(len(m.groups())))
			 		val = val_list		
	 			else:	
		 			m = re.compile(rule_ext_reg).search(val)			
		 			if m:
		 				val = m.group(len(m.groups()))
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
 