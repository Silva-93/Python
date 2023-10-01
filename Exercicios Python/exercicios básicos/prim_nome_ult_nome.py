""" 
    Faça um programa que leia um nome completo e mostre o primeiro e o último nome
"""

nome = str(input('Digite um nome completo.\nNome: '))
nome_lista = nome.split()  # dividindo o nome em uma lista

print(f'Seu primeiro nome é "{nome_lista[0]}" e seu último nome é "{nome_lista[len(nome_lista)-1]}" ')

