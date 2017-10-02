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
		c2 = Customer(98712387911, "Maria", 1180.50, True)
		# salvando no banco
		c1.save()
		c2.save()

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

		# outros testes, update e delete
		print()
		c1 = Customer(45612387911)
		c1.get_by_cpf()
		print(c1)
		print()
		c1.nm_customer = "João Paulo"
		c1.is_active = True
		c1.save()
		print(c1)
		c2 = Customer(12378945601)
		c2.get_by_cpf()
		c2.delete()

if __name__ == "__main__":
	teste = Testes()
	teste.main()