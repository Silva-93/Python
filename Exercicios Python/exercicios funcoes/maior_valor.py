""" 
    Faça um programa que tenha uma função que tenha o nome maiorValor, que receba vários parâmetros com valores inteiros. O programa deve analizar todos os valores e dizer qual é o maior deles. 
"""
def maiorValor(*num):
    maior_valor = max(num)
    total_digitos = len(num)
    print('-=' * 30)
    print('Analizando os valores')
    for valores in num:
        print(f'{valores}', end=' ')
    
    print(f'\nAo todo foram digitados {total_digitos} valores.')
    print(f'O maior valor foi {maior_valor}')


maiorValor(1,4,2,6,3,4,8,4,7)
maiorValor(1,4,7)
maiorValor(0)









