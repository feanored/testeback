#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 1 de out de 2017

@author: Eduardo
'''
from customer import Customer

class Testes:
	def main(self):
		# criando N registros
		c1 = Customer(45612387911, "João", 580.50, True)
		c2 = Customer(98712387912, "Maria", 1180.50, True)
		c3 = Customer(45678932113, "Zuleide", 700, True)
		
		# salvando no banco de dados
		c1.save()
		c2.save()
		c3.save()

		# obtendo clientes para cálculo da média
		clientes = Customer().get_by_saldo(560, (1500, 2700))
		qtde = len(clientes)
		if qtde > 0:
			total = 0
			for cliente in clientes:
				total += cliente.vl_total
				print(cliente)
				print()
			print("Média Final: R$ %.2f"%(total/qtde))
		else:
			print("Nenhum cliente cadastrado com essas especificações!")
		
if __name__ == "__main__":
	teste = Testes()
	teste.main()