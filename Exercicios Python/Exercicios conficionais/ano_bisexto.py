""" 
    Faça um programa que leia um ano qualquer e informe se o mesmo é um ano bisexto.
"""
from datetime import date
ano_atual = date.today().year

ano = int(input('Digite um ano para saber se ele é bisexto ou não.\nAno: '))

if ano == 0:
    print(ano_atual)

elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} foi BISEXTO.')

else:
    print(f'O ano de {ano} não foi um ano BISEXTO.')