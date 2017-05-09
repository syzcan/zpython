#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
reload(sys) 
sys.setdefaultencoding('utf8') 

def write(path,file_name,content):
	if not os.path.exists(path):
		os.makedirs(path)
	try:
		file = open(path+'/'+file_name,'wb')
		file.write(content)
		file.close()
	except Exception,e:
		print 'write error: '+path+'/'+file_name,e
	else:
		print 'write success: '+path+'/'+file_name

def read(file_path):
	try:
		file = open(file_path)
		content = file.read()
		file.close()
		return content
	except Exception,e:
		print 'read error: '+file_path,e
	else:
		print 'read success: '+file_path
						
