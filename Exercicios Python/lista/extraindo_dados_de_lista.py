""" 
    Crie um programa que vai ler vários números e coloca-los dentro de uma lista. Depois, disso, mostre:
    
    Quantos números foram digitados
    A lista de valores ordenada de forma decrescente
    Se o valor 5 foi digitado e está ou não dentro da lista
"""

lista_numerica = []

while True:
    lista_numerica.append(int(input('Digite um valor: ')))
    
    opcao = str(input('Quer continuar [S/N]')).strip().upper()
    if opcao in 'N':
        break

print('--' * 30)

if 5 not in lista_numerica:
    print('O número 5 não está na lista.')
else:
    print('O número 5 está na lista.')

print(f'Os números digitados foram: {lista_numerica}')
print(f'O total de números digitados foi: {len(lista_numerica)}')
lista_numerica.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista_numerica}')