""" 
    Crie um programa que vai ler vários números e colocar em uma lista. Depois disso crie duais listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final mostre o conteúdo das três listas geradas.
"""

lista_numeros = []
lista_pares = []
lista_impares = []

while True:
    lista_numeros.append(int(input('Digita um valor: ')))
    opcao = str(input('Quer continuar [S/N]?: ')).strip().upper()
    if opcao == 'N':
        break

for index, values in enumerate(lista_numeros):
    if values % 2 == 0:
        lista_pares.append(values)
    
    elif values % 2 != 0:
        lista_impares.append(values)

print('---' *30)
print(f'Os valores digitados foram: {lista_numeros}')
print(f'Os números pares da lista são: {lista_pares}')
print(f'Os números imparespares da lista são: {lista_impares}')