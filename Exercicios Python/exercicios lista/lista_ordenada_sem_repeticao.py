""" 
    Crie um programa onde o usuário possa digitar cingo valore numericos e cadastre-os em uma lista. Já na posição correta de inserção (sem o sort()). No final, mostre a lista ordenada na tela. 
"""

lista_numerica = []

for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    
    if cont == 0 or num > lista_numerica[-1]:
        lista_numerica.append(num)
        print('Adicionado no final da lista.')
    else:
        posicao = 0
        while posicao < len(lista_numerica):
            if num <= lista_numerica[posicao]:  #  Verifica dentro de cada posição se o número é menor ou igual a ele
                lista_numerica.insert(posicao, num)
                print(f'Adicionado na posição {posicao}.')
                break
            posicao += 1

print('=-=' * 30)
print (f'Os valores digitados em ordem foram: {lista_numerica}')    
