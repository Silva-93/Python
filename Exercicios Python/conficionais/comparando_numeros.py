""" 
    Escreva um programa que leia dois números inteiros e os compare, mostrando qual é o maior deles e se eles são iguais.
"""

primeiro = int(input('Digite o 1° número: '))
segundo = int(input('Digite o 2° número: '))

if primeiro > segundo:
    print(f'O primerio número "{primeiro}" é maior que o segundo número "{segundo}".')

elif segundo > primeiro:
    print(f'O segundo número "{segundo}" é maior que o primeiro número "{primeiro}".')

elif primeiro == segundo:
    print('Os dois números são iguas.')

else:
    print('Por favor, digite um número.')