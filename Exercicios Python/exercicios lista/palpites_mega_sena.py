""" 
    Faça um programa que ajude um jogador da mega sena a criar palpites. O programa irá perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para criar cada jogo, tudos um uma lista composta.
"""

from random import randint
from time import sleep

lista = []
jogo = []

print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)

quantidade = int(input('Quantos jogos você quer jogar?: '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    total += 1

print(f'{"-"*3} Sorteando {quantidade} jogos {"-"*3}')
for i, l in enumerate(jogo):
    sleep(.8)
    print(f'{i+1}: {l}')