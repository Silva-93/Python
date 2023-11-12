""" 
    Faça um programa que tenha uma função chamada contador(), que receva três parâmetros; inicio, fim, passo. O programa deve realizar três contagens atravéis da função criada. 

    De 1 até 10 de 1 em 1
    De 10 até 0 de 2 em 2
    Uma contagem personalizada
"""

from time import sleep



def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    
    if passo == 0:
        passo = 1

    print('-=' * 20)

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)  # flush=True tira o buffer de tela
            sleep(.5)
            cont += passo
        print('FIM!')

    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(.5)
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)

print('Agora é sua vez de fazer um contador.')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)

