""" 
    Escreva um programa que leia um número inteiro e peça para o usuário escolher qual base númerica será a base de conversão
    1 - Binário
    2 - Octal
    3 - Hexadecimal
"""

num = int(input('Digite um número: '))


print(''' Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')

base = int(input('Escolha uma opção: '))

if base == 1:
    print(f'O número {num} convertido para BINÁRIO é: {bin(num)[2:]}')

elif base == 2:
    print(f'O número {num} convertido para OCTAL é: {oct(num)[2:]}')

elif base == 3:
    print(f'O número {num} convertido para HEXADECIMAL é: {hex(num)[2:]}')

else:
    print('Por favor, escolha uma das três opções. acima')