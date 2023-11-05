""" 
    Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sortear() e somarPar(). A primeira função vai sortear cinco números e coloca-los dentro de uma lista e a segunda função vai mostrar a soma de todos os valores pares sorteador pela função sortear()
"""

from random import randint
from time import sleep

def sortear(lista):
    print(f'Soretando os 5 valores da lista: {lista}', end=' ')
    for _ in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
        print(f'{num}', end=' ', flush=True)
        sleep(.3)
    print('FIM')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma de todos os valores pares da lista {numeros} é: {soma}')

numeros = []
sortear(numeros)
somaPar(numeros)