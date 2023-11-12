""" 
    crie um programa que cria uma matriz de dimensão 3x3 e preencha por valores lidos pelo teclado
"""

matriz = [[0,0,0],[0,0,0],[0,0,0]]

# Alimentando a matriz com os números
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]: '))

print('--' * 30)

# formatando a matriz para mostra na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()