""" 
    Crie um programa que vai gerar cinco números aleatórios e colocar um uma tupla. Depois disso, mostre a listagem de números e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10))
maior = max(numeros)
menor = min(numeros)

print(f'Os valores sorteados foram: ', end=' ')
for num in numeros:
    print(f'{num}', end=' ')

print(f'\nO maior número da tupla é: {maior}')
print(f'O menor número da tupla é: {menor}')

