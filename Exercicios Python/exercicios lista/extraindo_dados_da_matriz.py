""" 
    crie um programa que cria uma matriz de dimensão 3x3 e preencha por valores lidos pelo teclado e mostre:

    A soma de todos os valores pares
    A soma dos valores da terceira coluna
    O maior valor da segunda linha
"""

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = soma_coluna = 0

# Alimentando a matriz com os números
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]: '))

print('--' * 30)

# formatando a matriz para mostra na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()


print(f'A soma de todos os valores pares é: {soma_pares}')

print(f'A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')

print(f'O maior valor da segundalinha é: {max(matriz[1][0], matriz[1][1], matriz[1][2])}')