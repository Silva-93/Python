""" 
    Faça um programa que gere um número aleatório de 0 à 5 o armazene e faça com que o usuário adivinhe o número gerado
"""
from random import randint
from time import sleep

num = int(input('Digite um número: '))
num_sorte = randint(0, 5)

if num == num_sorte:
    print('Sorteando...')
    sleep(3)
    print('Acertou!')

else:
    print('Sorteando...')
    sleep(3)
    print(f'Você errou! O número sorteado foi {num_sorte}.')