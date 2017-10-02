#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 1 de out de 2017

@author: Eduardo
'''
import pymysql as db

class Conexao:
	def __init__(self):
		'''(Conexao) -> None'''
		self.con = db.connect(host='localhost', 
							  user='root',
							  passwd='koopa',
							  db='testes',
							  cursorclass=db.cursors.DictCursor)
		self.cursor = None

	def get_cursor(self):
		'''(Conexao) -> pymysql.cursor'''
		if self.cursor is None:
			self.cursor = self.con.cursor()
		return self.cursor

	def commit(self):
		'''(Conexao) -> None'''
		self.con.commit()

	def close(self):
		'''(Conexao) -> None'''
		self.con.close()
