""" 
     Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
 
    Quantas vezes apareceu o valor 9.
    Em que posição foi digitado o primeiro valor 3.
    Quais foram os números pares. 

"""
numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))

print(f'Você digitou os valores: {numeros}')
print(f'O numero nove foi digitado {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O número três está na {numeros.index(3)+1}° posição')
else:
    print('O número três não foi digitado.')

print(f'Os números pares foram: ', end='')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')
