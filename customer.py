#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 1 de out de 2017

@author: Eduardo
'''
from customer_model import CustomerModel
from conexao import Conexao

class Customer(CustomerModel):
	def __init__(self, cpf=0, nome="", saldo=0, ativo=0):
		'''(Customer, int, str, float, bool) -> None'''
		super().__init__(cpf, nome, saldo, ativo)

	def __call__(self):
		'''(Customer) -> None'''
		super().__call__()

	def conecta(self):
		'''(Customer) -> None'''
		self.con = Conexao()

	def desconecta(self):
		'''(Customer) -> None'''
		self.con.close()

	def save(self):
		'''(Customer) -> None'''
		if self.id_customer is None:
			self.insert()
		else:
			self.update()

	def insert(self):
		'''(Customer) -> None'''
		sql = "INSERT INTO %s " %(self.tabela)
		sql += "(cpf_cnpj, nm_customer, is_active, vl_total) "
		sql += "VALUES (%s, '%s', %s, %s)" %(self.cpf_cnpj, self.nm_customer, 
										 int(self.is_active), self.vl_total)
		print(sql)
		try:
			self.conecta()
			cursor = self.con.get_cursor()
			cursor.execute(sql)
			self.con.commit()
			cursor.execute("SELECT LAST_INSERT_ID() as id")
			dados = cursor.fetchone()
			self.id_customer = dados["id"]
		finally:
			self.desconecta()

	def update(self):
		'''(Customer) -> None'''
		sql = "UPDATE %s SET " %(self.tabela)
		sql += "cpf_cnpj = %s, " %(self.cpf_cnpj)
		sql += "nm_customer = '%s', " %(self.nm_customer)
		sql += "is_active = %s, " %(int(self.is_active))
		sql += "vl_total = %s " %(self.vl_total)
		sql += "WHERE id_customer = %s" %(self.id_customer)
		try:
			self.conecta()
			cursor = self.con.get_cursor()
			cursor.execute(sql)
			self.con.commit()
		finally:
			self.desconecta()

	def delete(self):
		'''(Customer) -> None'''
		if self.id_customer is None:
			return
		sql = "DELETE FROM %s " %(self.tabela)
		sql += "WHERE id_customer = %s" %(self.id_customer)
		try:
			self.conecta()
			cursor = self.con.get_cursor()
			cursor.execute(sql)
			self.con.commit()
		finally:
			self.desconecta()

	def load_from_dados(self, dados):
		'''(Customer, dict) -> Customer'''
		customer = Customer(int(dados["cpf_cnpj"]), dados["nm_customer"],
							float(dados["vl_total"]), bool(dados["is_active"]))
		customer.id_customer = dados["id_customer"]
		return customer

	def get_by_cpf(self):
		'''(Customer) -> None'''
		sql = "SELECT * FROM %s WHERE cpf_cnpj = %s" %(self.tabela, self.cpf_cnpj)
		try:
			self.conecta()
			cursor = self.con.get_cursor()
			cursor.execute(sql)
			dados = cursor.fetchone()
			if dados is not None:
				aux = self.load_from_dados(dados)
				self.id_customer = aux.id_customer
				self.nm_customer = aux.nm_customer
				self.vl_total = aux.vl_total
				self.is_active = aux.is_active
		finally:
			self.desconecta()

	def get_by_saldo(self, saldo=None, ids=()):
		'''(Customer, float, tuple) -> list'''
		sql = "SELECT * FROM %s WHERE is_active = 1" %(self.tabela)
		if not saldo is None:
			sql += " AND vl_total > %s"%(saldo)
		if len(ids) == 2:
			sql += " AND id_customer >= %s AND id_customer <= %s" %(ids[0], ids[1])
		sql += " ORDER BY vl_total DESC"
		customers = []
		try:
			self.conecta()
			cursor = self.con.get_cursor()
			cursor.execute(sql)
			dados = cursor.fetchall()
			for linha in dados:
				customers.append(self.load_from_dados(linha))
		finally:
			self.desconecta()
		return customers
