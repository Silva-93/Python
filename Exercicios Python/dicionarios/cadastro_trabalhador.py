""" 
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de zero, o dicionário também receberá o ano de contratação e o salário. Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar. 
"""
from datetime import date

ano_atual = date.today().year

dados = {}
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - dados['nascimento']
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - ano_atual)

print('--' * 30)

for k, v in dados.items():
    print(f'{k} tem o valor de {v}')