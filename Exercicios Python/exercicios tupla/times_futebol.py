""" 
    Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

    Os 5 primeiros.
    Os últimos 4 colocados.
    Times em ordem alfabética.
    Em que posição está o time da Internacional.

"""

times = ('Botafogo', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Grêmio', 'Palmeiras', 'Atlético-MG', 'Fortaleza', 'Fluminense', 'São-Paulo', 'Cuiabá', 'Bahia', 'Internacional', 'Corinthians', 'Cruzeiro', 'Goiás', 'Vasco', 'Santos', 'Coritiba', 'América-MG')

print('=-=' * 30)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('=-=' * 30)
print(' ')

print('=-=' * 30)
print(f'O quatros últimos colocados são: {times[-4:]}')
print('=-=' * 30)
print(' ')

print('=-=' * 30)
print(f'A lista de times em ordem alfabética é: {sorted(times)}')
print('=-=' * 30)
print(' ')

print('=-=' * 30)
print(f'O Internacional está na posição: {times.index("Internacional")}')
print('=-=' * 30)
