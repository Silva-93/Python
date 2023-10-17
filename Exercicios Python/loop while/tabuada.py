""" 
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompindo quando o usuário digitar um número negativo.
"""

while True:
    numero = int(input('Digite um número para saber sua tabuada: '))

    if numero < 0:
        print('ENCERRANDO O PROGRAMA.')
        break

    for x in range(1, 11):
        print(f'{numero} x {x} = {numero * x}')