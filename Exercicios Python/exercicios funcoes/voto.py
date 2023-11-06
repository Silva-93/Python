""" 
    Crie um programa que tenha uma função chamada voto() que vai recever como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa tem voto NEGADO, APCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    print('--' * 20)
    if 16 == idade < 18 or idade >= 65:
        return f'Com a idade de {idade} o voto é OPCIONAL.'
    
    elif idade < 16:
        return f'Com a idade de {idade} o voto é NEGADO.'
    
    else:
        return f'Com a idade de {idade} o voto é OBRIGATÓRIO.'

nascimento = int(input('Ano de nascimento: '))

print(voto(nascimento))

