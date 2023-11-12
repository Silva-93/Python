""" 
    Escreva um programa que pergunte a quantidade de KMs percorridos por um carro alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

diarias = int(input('Alugou o carro por quantos dias?\nDias alugados: '))

km = float(input('Quandtos quilômetros você rodou com o carro?\nKMs: '))

custo_diarias = (diarias * 60) + (km * 0.15)


print(f'Você rodou {km}kms seu custo será {custo_diarias}')