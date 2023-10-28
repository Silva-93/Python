""" 
    Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.
"""

lista_numerica = [[], []]

for x in range(1, 8):
    num = int(input(f'Digite {x}° número: '))

    if num % 2 == 0:
        lista_numerica[0].append(num)
    else:
        lista_numerica[1].append(num)

lista_numerica[0].sort()
lista_numerica[1].sort()

print(f'A lista com os valores pares foi: {lista_numerica[0]}')
print(f'A lista com os valres impares foi: {lista_numerica[1]}')