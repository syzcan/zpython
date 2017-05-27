#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
reload(sys) 
sys.setdefaultencoding('utf8') 

spiders = []			
for i in os.listdir(os.getcwd()):
	if i.startswith('spider_') and os.path.isfile(i):
		spiders.append(i)
		
for i in range(len(spiders)):
	print i+1,spiders[i]	

cmd = raw_input('\r\nEnter num:')
os.system('python '+spiders[int(cmd)-1])