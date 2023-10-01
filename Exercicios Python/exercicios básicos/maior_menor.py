""" 
    Faça um programa que leia três números e mostre qual é o maior dentre eles
"""

n1 = int(input('Digite um número.\n1° número: '))
n2 = int(input('Digite um número.\n2° número: '))
n3 = int(input('Digite um número.\n3° número: '))
numeros = [n1, n2, n3]

print(f'O maior número foi {max(numeros)} e o menor número foi {min(numeros)}')
