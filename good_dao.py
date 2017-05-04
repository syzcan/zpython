#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
import mysql.connector
# from mysql.connector import FieldType
reload(sys) 
sys.setdefaultencoding('utf8') 

cnx = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', password='Zong', database='test')

class Good:
	def __init__(self, id, name, price):
		self.id = id
		self.name = name
		self.price = price
		pass

def insert(good):
	cursor = cnx.cursor()

	sql = ("insert into good(name,price) values(%s,%s)")
	params = (good.name,good.price)

	cursor.execute(sql,params)
	cnx.commit()
	cursor.close()

def delete(good):
	cursor = cnx.cursor()

	sql = ("delete from good where id=%s")
	params = (good.id)

	cursor.execute(sql,params)
	cnx.commit()
	cursor.close()

def update(good):
	cursor = cnx.cursor()

	sql = ("update good set name=%s,price=%s where id=%s")
	params = (good.name,good.price,good.id)

	cursor.execute(sql,params)
	cnx.commit()
	cursor.close()	

def select(good):
	cursor = cnx.cursor()

	sql = ("select id,name,price from good where 1=1 ")
	if good != None and good.name != None:
		sql += "and name like '%"+good.name+"%'"
	cursor.execute(sql)
	goods = []
	for (id,name,price) in cursor:
  		goods.append(Good(id,name,price))

	cursor.close()
	return goods

def write():
	goods = select(Good(None,None,None))
	count = 1
	for good in goods:
		if not os.path.exists('c:/zlogs/good'):
			os.makedirs('c:/zlogs/good')
		try:
			file = open('c:/zlogs/good/'+str(good.id)+good.name.replace('|','').replace('?','')+'.txt','wb')
			file.write(str(good.id)+'\n'+good.name+'\n'+str(good.price))
			file.close()
		except:
			print '错误：'+good.name
		print count,'写入good：'+str(good.id)+good.name+'.txt'
		count += 1	

# for i in range(0,10):
# 	insert(Good(None,'电脑',500))

# goods = select(Good(None,None,None))
# for good in goods:
# 	print(good.name)

write()