""" 
    Faça um programa que tenha uma função chamada ficha, que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.  
"""

def ficha(nome='<desconhecido', gol=0):
    print(f'O jogagor {nome} fez {gol} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gol = str(input('Números de gols: '))


if gol.isnumeric():
    gol = int(gol)

else:
    gol = 0

if nome == '':
    ficha(gol=gol)

else:
    ficha(nome, gol)













