""" 
    Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
    
    Qual é o total gasto na compra.
    Quantos produtos custam mais de R$ 1000,00
    Qual é o nome do produto mais barato.

"""

preco_total = mais_mil = menor_preco = cont = 0
nome_produto = ' '
while True:
    produto = str(input('Digite um produto: '))
    preco = float(input('Digite o preço R$: '))
    cont += 1
    preco_total += preco

    if preco > 1000:
        mais_mil += 1
    
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        nome_produto = produto

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]')).strip().upper()[0]
    
    if opcao == 'N':
        break

print(f'Quantidade de produtos comprados que custam mais de R$: 1000,00 é: {mais_mil}')
print(f'O total da compra foi: {preco_total}')
print(f'O produto mais barato foi "{nome_produto}" e seu preço é "{menor_preco}"')