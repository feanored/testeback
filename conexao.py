#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 1 de out de 2017

@author: Eduardo
'''
import MySQLdb as db

class Conexao:
	def __init__(self):
		self.con = db.connect(host='localhost', user='root', passwd='koopa', db='testes')
		self.cursor = None

	def set_cursor(self):
		self.cursor = self.con.cursor()

	def get_cursor(self):
		if self.cursor is None:
			self.set_cursor()
		return self.cursor

	
