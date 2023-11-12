""" 
    Escreva um programa que leia um número e identifique se ele é par ou impar
"""

numero = int(input('Digite um número para saber se ele é PAR ou IMPAR.\nNúmero: '))

if numero % 2 == 0:
    print('Este número é \033[34mPAR\033[0;0m')

else:
    print('Este número é \033[32mIMPAR\033[0;0m')
