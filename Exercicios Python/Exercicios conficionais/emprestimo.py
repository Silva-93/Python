""" 
    Faça um programa para aprovar um empréstimo bancário para comprar uma casa. Pergunte pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    A prestação mensal não pode exceder 30% do salário ou então o emprestimo será negado.
"""

valor_casa = float(input('Qual o valor da casa? R$: '))
salario = float(input('Qual o seu salário? R$: '))
anos = int(input('Por quantos anos você vai pagar a casa? Anos: '))
prestacao = valor_casa / (anos * 12)
nao_pode_exceder = (salario * 30) / 100

print(' ')

print(f'Valor da casa: {valor_casa}')
print(f'Seu salário: {salario}')
print(f'Quantidade de anos: {anos}')
print(f'Valor das prestações: {prestacao:.2f}')

print(' ')

if prestacao > nao_pode_exceder:
    print(f'Não pode financiar a casa. As prestações ultrapassarão o valor de 30% do seu salário.')
else:
    print('Pode financiar.')