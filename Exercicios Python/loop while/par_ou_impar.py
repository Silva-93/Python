""" 
    Faça um programa que jogue par ou impar com o computador. O jogo só será imterrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

vitorias = 0
while True:
    jogador = str(input('Par ou Impar [P/I]: ')).upper()
    valor = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = valor + computador

    if jogador == 'P':
        if total % 2 == 0:
            print(f'Jogador jogou {valor} e o computador jogou {computador}. O TOTAL é {total} PAR.')
            print('JOGADOR GANHOU!!!')
            vitorias += 1
        else:
            print(f'Computador jogou {computador} e o jogador jogou {valor}. O TOTAL é {total}. IMPAR')
            print(f'Você perdeu.')
            break
    
    elif jogador == 'I':
        if total % 2 != 0:
            print(f'Jogador jogou {valor} e o computador jogou {computador}. O TOTAL é {total} IMPAR.')
            print(f'JOGADOR GANHOU!!')
            vitorias += 1
        else:
            print(f'Computador jogou {computador} e o jogador jogou {valor}. O TOTAL é {total}. PAR')
            print('Você perdeu.')
            break

print(f'O jogador venceu {vitorias} vezes')
        


