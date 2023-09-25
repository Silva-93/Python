""" 
    Digite um programa que leia um número e exiba a tabuada de 1 a 10
"""

# numero = int(input('Digite um número para saber sua tabuada.\nNúmero: '))

# for x in range(1, 11):
#     print(f'{numero} x {x} = {numero * x}')

def tabuada(n):
    return [n*x for x in range(1, 11)]

tab5 = tabuada(5)
print(tab5, end=' ')