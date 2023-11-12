""" 
    Escreva um programa que leia um nome e informe se há um n0ome silva dentro dele
"""

nome = str(input('Digite um nome completo.\nNome: ')).lower()

print(f'Seu nome tem silva? {"silva" in nome.lower()}')