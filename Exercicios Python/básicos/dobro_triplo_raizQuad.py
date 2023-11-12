""" 
    Faça um programa que leia um número e mostre na tela seu dobro, triplo e raiz quadrada.
"""

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print(f'O dobro de {numero} é: {dobro}\nO triplo de {numero} é: {triplo}\nA raiz quadrada de {numero} é: {raiz_quadrada:.2f}.')