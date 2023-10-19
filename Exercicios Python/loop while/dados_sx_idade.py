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
    sexo = str(input('Sexo [M/F]: ')).upper()
    opcao = str(input('Quer continuar? [S/N]: ')).upper()

    if opcao != 'N':    
        if sexo == 'F' and idade < 20:
            mulher_menor_20 += 1
        
        elif sexo == 'M':
            total_homens += 1

        elif idade > 18:
            mais_18 += 1
        
    else:
        break

print(f'Ao todo foram {mais_18} pessoas maiores de 18 cadastradas.')
print(f'Ao todo foram {total_homens} homens cadastrados.')
print(f'Ao todo foram {mulher_menor_20} mulheres com menos de 20 anos cadastradas.')