""" 
    Faça um programa que leia 5 valores numericos guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respequitivas posições na lista.
"""

numeros = []

for num in range(1, 6):
    num = int(input('Digite um número: '))
    numeros.append(num)
    maior = max(numeros)
    menor = min(numeros)
    posi_maior = numeros.index(maior)
    posi_menor = numeros.index(menor)

print('=-=' * 30)

print(f'Você digitou os valores: {numeros}')
print(f'O maior valor digitado foi "{maior}" e sua posição na lista é na {posi_maior + 1}° posição')
print(f'O maior valor digitado foi "{menor}" e sua posição na lista é na {posi_menor + 1}° posição')
""" print(posi_maior)
print(posi_menor) """