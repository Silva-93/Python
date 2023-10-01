""" 
    Escreva um programa que leia a velocidade de um carro. Caso ele ultrapasse 80km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$: 7,00 por cada km ultrapassado. 
"""

km = int(input('Digite sua valocidade: '))
multa = (km - 80) * 7

if km <= 80:
    print('\033[32mDirija com segurança\033[0;0m')
else:
    print(f'\033[31mMultado! Você pagará\033[0;0m {multa}')