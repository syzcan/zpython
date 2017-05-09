#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
reload(sys) 
sys.setdefaultencoding('utf8') 
import re
from zlibs import file_util
from zlibs import craw_util
from zlibs.craw_util import craw_rule

craw_url = "http://www.bilibili.com/video/music.html"

img_rule = craw_rule("imgs","img","attr","src","array")

while True:
	cmd = raw_input("input craw_url:")
	if cmd != '':
		craw_url = cmd
	data = craw_util.craw_detail(craw_url,[img_rule])
	for img in data['imgs']:
		m = re.search(r'[^/]*\.(jpg|png)$',img)
		if m:	
			file_util.write('c:/zlogs/img',m.group(0),craw_util.request_get(img).content)			
		
		