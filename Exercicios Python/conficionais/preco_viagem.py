""" 
    Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 para viagens até 200km e R$ 0,45 para viagens acima de 200km
"""

distancia = float(input('Digite a distância da viagem em KMs: '))
preco_maoir = 0.50
preco_menor = 0.45

""" if distancia <= 200:
    print(f'Sua viagem vai custar R$: {distancia * preco_maoir}')
else:
    print(f'Sua viagem vai custar R$: {distancia * preco_menor}')
"""
# Resolução com operador tenário

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O valor da sua viagem será de R$: {preco}')
