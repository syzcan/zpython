#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys
import mysql.connector
import re
# from mysql.connector import FieldType
reload(sys) 
sys.setdefaultencoding('utf8') 

cnx = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', password='Zong', database='test')

def insert(table,data):
	cursor = cnx.cursor()

	sql = "insert into "+ table +"("
	for key in data.keys():
		sql += key + ","
	sql,number = re.subn(",$","",sql)	
	sql += ") values("
	for key in data.keys():
		sql += "%s,"
	sql,number = re.subn(",$","",sql)	
	sql += ")"

	params = []
	for key in data.keys():
		params.append(data[key])
	# list转元组 
	params = tuple(params)	

	cursor.execute(sql,params)
	cnx.commit()
	cursor.close()

def delete(table,id_data):
	cursor = cnx.cursor()

	sql = "delete from "+ table +" where 1=1"
	for key in id_data.keys():
		sql += " and " + key + "=%s"

	params = []
	for key in id_data.keys():
		params.append(id_data[key])
	params = tuple(params)

	cursor.execute(sql,params)
	cnx.commit()
	cursor.close()

def update(table,data,id_data):
	cursor = cnx.cursor()

	sql = "update " + table + " set "
	for key in data.keys():
		sql += key + "=%s,"
	sql,number = re.subn(",$","",sql)
	sql += " where 1=1"
	for key in id_data.keys():
		sql += " and " + key + "=" + id_data[key]
	
	params = []
	for key in data.keys():
		params.append(data[key])
	params = tuple(params)

	cursor.execute(sql,params)
	cnx.commit()
	cursor.close()	

def select(table,data=None):
	#returns rows as dictionaries
	cursor = cnx.cursor(dictionary=True)

	sql = "select * from " + table + " where 1=1"
	if data != None:
		for key in data.keys():
			sql += " and " + key + "=%s"

	params = []
	if data != None:
		for key in data.keys():
			params.append(data[key])
	params = tuple(params)

	cursor.execute(sql,params)
	datas = cursor.fetchall()
	cursor.close()
	return datas
