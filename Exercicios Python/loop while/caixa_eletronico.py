""" 
    Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

    Obs.: O caixa só possui cédulas de 50, 20, 10 e 1.
"""

print('+=======================================+')
print('|               BANCO CEV               |')
print('+=======================================+')


valor = int(input('Qual valor você quer sacar.\nR$: '))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de {cedula}.')
        if cedula == 50:
            cedula = 20
        
        elif cedula == 20:
            cedula = 10
        
        elif cedula == 10:
            cedula =1
        
        total_cedula = 0

        if total == 0:
            break