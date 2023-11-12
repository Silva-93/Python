""" 
    Crie um programa que gerencie o aproveitamento de vários jogadores de futebol. O programa vai ler os nomes do jogadores, quantas partidas eles jogaram. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. Inclua um sistema de vizualização de detalhes de aproveitamento de cada jogador.  
"""

from time import sleep

time = []
dados = {}
partidas = []
dados['gols'] = []
dados['total'] = 0

# Cadastrando os dados dos jogadores
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    
    jogos = int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
    
    partidas.clear()

    for x in range(1, jogos + 1):
        partidas.append(int(input(f'Quantos gols na partida {x+1}: ')))
        dados['gols'] = partidas[:]
        dados['total'] = sum(dados['gols'])

    time.append(dados.copy())

    opcao = str(input('Quer continuar? [S/N]: ')).upper()
    while True:
        if opcao in 'SN':
            break
        print('Por favor, responda apenas "S" ou "N".')
        
    if opcao == 'N':
        break

# Cabeçalho
print('-=' * 30)
print('Cod  ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')

print()

# Exibindo os dados dos jogadores
print('--' * 30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 30)

# Escolhendo os dados dos jogadores

while True:
    buscar = int(input('De qual jogador você quer vizualizar os dados? (999 para parar)\nDados do jogador: '))
    if buscar == 999:
        break

    if buscar > len(time):
        print(f'ERRO! Não existe um jogador com o código da busca {buscar}.')

    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[buscar]["nome"]}')
        for i, g in enumerate(time[buscar]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')

    print('--' * 30)

print(' FIM !!!')














