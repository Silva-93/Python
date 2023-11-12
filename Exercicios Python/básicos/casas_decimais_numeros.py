""" 
    Escreva um programa que leia um número de 0 à 9999 e mostre na tela cada um dos digitos separados
"""

numero = int(input('Digite um núemro.\nNúmero: '))

unidade = numero // 1 % 10  # número dividido por 1 e com o módulo de 10, o que sobrar é a unidade
dezena = numero // 10 % 10 
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Analisando o número: {numero}')
print(f'Sua unidade é: {unidade}')
print(f'Sua dezena é: {dezena}')
print(f'Sua centena é: {centena}')
print(f'Seu milhar é: {milhar}')