#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 1 de out de 2017

@author: Eduardo
'''
class CustomerModel:
	def __init__(self, cpf, nome, saldo, ativo):
		'''(CustomerModel, int, str, float, bool) -> None'''
		self.id_customer = None
		self.cpf_cnpj = cpf
		self.nm_customer = nome
		self.vl_total = saldo
		self.is_active = ativo
		self.con = None
		self.tabela = "tb_customer_account"

	def __call__(self):
		'''(CustomerModel) -> None'''
		self.con = None
		self.tabela = "tb_customer_account"

	def __str__(self):
		'''(CustomerModel) -> str'''
		txt = "Nome: %s\nCPF/CNPJ: %s\nSaldo: R$ %.2f"%(self.nm_customer, self.cpf_cnpj, self.vl_total)
		return txt
