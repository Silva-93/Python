""" 
    Digite um programa que leia um número e exiba a tabuada de 1 a 10
"""

numero = int(input('Digite um número para saber sua tabuada.\nNúmero: '))

for x in range(1, 11):
    print(f'{numero} x {x} = {numero * x}')
