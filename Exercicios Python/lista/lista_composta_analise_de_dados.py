""" 
    Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

    Quantas pessoas foram cadastradas.
    Uma lista com as pessoas mais pesadas. 
    Uma lista com as pessoas mais leves.
"""

temp = []
dados = []
maior_peso = menor_peso = 0
total_pessoas = 0

while True:
    temp.append(str(input('Nome: ')))
    total_pessoas += 1

    temp.append(float(input('Peso: ')))
    
    if len(dados) == 0:
        maior_peso = menor_peso = temp[1]
    else:
        if temp[1] > maior_peso:
            maior_peso = temp[1]
        
        if temp[1] < menor_peso:
            menor_peso = temp[1]
    
    dados.append(temp[:])
    temp.clear()

    opcao = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    if opcao == 'N':
        break

print('---' * 30)
print(f'Ao todo foram cadastrados {total_pessoas} pessoas')

print(f'O maior peso foi {maior_peso}Kg de ', end=' ')
for d in dados:
    if d[1] == maior_peso:
        print(f'{d[0]}', end=' ')
print()

print(f'O menor peso foi {menor_peso}Kg de ', end=' ')
for d in dados:
    if d[1] == menor_peso:
        print(f'{d[0]}', end=' ')
print()
