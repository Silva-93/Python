""" 
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardadno os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

    Quantas pessoas foram cadastradas. 
    A média de idade. 
    Uma lista de mulheres. 
    Uma lista com idade acima da média. 
"""

galera = []
pessoa = {}
soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Por favor, digite apenas "M" ou "F".')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        opcao = str(input('Quer continuar [S/N]: ')).upper()
        if opcao in 'SN':
            break
        print('Por favor, digite apenas "S" ou "N".')
    if opcao == 'N':
        break

media = soma / len(galera)

print('---' * 30)
print(f'A média de idade é: {media:.2f} anos.')
print(f'Ao todo foram {len(galera)} pessoas cadastradas.')
print('As mulheres cadastradas foram: ', end='')

for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')

print('\nA lista de pessoas que estão com a idade acima da média é: ')

for p in galera:
    if p['idade'] > media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ACABOU!!!')
