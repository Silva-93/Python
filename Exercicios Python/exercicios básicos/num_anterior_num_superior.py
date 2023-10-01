""" 
    Faça um programa que leia um número e mostre na tela seu antecessor e seu sucessor.
"""
numero = int(input('Digite um número.\nNúmero: '))

num_anterior = numero - 1
num_superior = numero + 1

print(f'O número digitado foi {numero}, seu antecessor é {num_anterior} e seu sucessor é {num_superior}.')