""" 
    Faça um programa que leia o comprimento de um catito oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
"""
import math

catetoOP = float(input('Cateto Oposto: '))

catetoAD = float(input('Cateto Adjacente: '))

hip = math.hypot(catetoOP, catetoAD)
print(f'{hip:.2f}')

# Mesmo resultado sem a importação

# hipotenusa = (catetoOP**2 + catetoAD**2) ** (1/2)

# print(f'A hipotenusa é igual a: {hipotenusa:.2f}')
