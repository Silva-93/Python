""" 
    Faça um programa que leia o preço de um produto e mostre seu novo proço com 5% de desconto.
"""

preco = float(input('Digite o preço do produto para ver seu desconto.\nPreço: '))
desconto_5 = (preco * 5) / 100
preco_desconto = preco - desconto_5

print(f'O produto vale R$: {preco} com o desconto de 5%, seu valor diminiu {desconto_5}. Com isso seu valore passa a ser R$:{preco_desconto}')
