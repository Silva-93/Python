""" 
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deve perguntar ao usuário se quer ou não continuar. No final mostre:
    
    Quantas pessoas tem mais de 18 anos.
    Quantos homens foram cadastrados. 
    Quantas mulheres tem menos de 20 anos.
"""
total_homens = mulher_menor_20 = mais_18 = 0
while True:
    print('--------------------------')
    print('   CADASTRE UMA PESSOA    ')
    print('--------------------------')

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    
    if idade >= 18:
        mais_18 += 1
    
    if sexo in 'M':
        total_homens += 1
    
    if sexo in 'Ff' and idade < 20:
        mulher_menor_20 += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if opcao == 'N':
        break

print(f'Ao todo foram {mais_18} pessoas maiores de 18 cadastradas.')
print(f'Ao todo foram {total_homens} homens cadastrados.')
print(f'Ao todo foram {mulher_menor_20} mulheres com menos de 20 anos cadastradas.')