""" 
    Crie um programa onde o usuário possa digitar vários valores numericos e cadastreos em uma lista. Caso o número já exista na lista, ele não será adicionado. No final, será exibido todos os valores únicos em ordem crescente.
"""

numeros = []
while True:
    num = int(input('Digite um valor: '))

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).upper()

    if num not in numeros:
        numeros.append(num)
    else:
        print(f'O número {num} já está na lista e não será adicionado novamente.')

    if opcao == 'N':
        break

print('=-=' * 30)
numeros.sort()
print(f'Você digitou os valores: {numeros}')