""" 
    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador, quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 
"""
from time import sleep

dados = {}
dados['nome'] = str(input('Nome do jogador: '))
dados['gols'] = []
dados['total'] = 0

partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))

for x in range(1, partidas + 1):
    dados['gols'].append(int(input(f'Quantos gols na partida {x}: ')))
    dados['total'] = sum(dados['gols'])

print('--' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor de {v}')
print('--' * 30)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for y in range(partidas):
    sleep(1)
    print(f'   => Na partida {y+1}, fez {dados["gols"][y]} gols. ')

print()
print(f'O total de gols realizado foi {dados["total"]} gols.')














