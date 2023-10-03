""" 
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se ele precisa se alistar ou se já passou o tempo de alistamento.
    Seu programa também deve mostrar o tempo que falta para o alistamento e o tempo que já pasou.
"""
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))



idade = ano_atual - ano_nascimento

if idade < 18:
    print(f'Você tem {idade} anos, faltam {18 - idade} anos pra se alistar.')

if idade == 18:
    print(f'Você tem {idade} anos, aliste-se imediatamente.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você tem {idade} anos, já passou {idade - 18} anos do seu alistamento. ')
    print(f'Seu alistamento foi em {ano_atual - saldo}')

else:
    ...