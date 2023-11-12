""" 
    Faça um programa que calcule o valor a ser pago pro um produto.
    Consigerando seu preço normal e condição de pagamento. 
    
    À vista/cheque -> 10% de desconto
    À vista no cartão -> 5% de desconto
    Em até 2x no cartão -> Preço normal
    3x ou mais vezes no cartão -> 20% de juros
"""

print('========== Lojas Jouber ==========')

preco = float(input('Preço das compras.\nR$: '))

print('''Formas do pagamento:
      [ 1 ] À vista/cheque
      [ 2 ] À vista no cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão
''')
forma_pagamento = int(input('Forma de pagamento: '))

desconto_10 = (preco * 10) / 100
desconto_5 = (preco * 5) / 100
juros = (preco * 20) / 100

if forma_pagamento == 1:
    print(f'Você terá 10% de desconto, o valor a pagar é: {preco - desconto_10}')

elif forma_pagamento == 2:
    print(f'Você terá 5% de desconto, o valor a pagar é: {preco - desconto_5}')

elif forma_pagamento == 3:
    print(f'Sua compra será parcelada em 2x de R$: {preco/2:.2f} .')
    print(f'O preço a pagar é: {preco}')

elif forma_pagamento == 4:
    qtd_parcelas = int(input('Quantas parcelas?\nParcelas: '))
    
    parcelas = preco / qtd_parcelas

    print(f'Sua compra será parcelada em {qtd_parcelas}x de {parcelas:.2f} com juros de 20%.')
    print(f'O valor a pagar é: {preco + juros}.')

else:
    print('Digite uma das três opções acima.')