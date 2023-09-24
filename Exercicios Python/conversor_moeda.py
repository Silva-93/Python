""" 
    Faça um programa que leia a quantidade de dinheiro de uma pessoa e exiba o quanto seria em dolares.
"""

dolares = 4.94
real = float(input('Quantos reais você tem?\nR$: '))
real_dolar = real / dolares


print(f'{real} equivalem a {real_dolar:.2f} dolares')