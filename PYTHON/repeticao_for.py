'''
    Iterável -> str, range, etc (__iter__)
    Iterador -> quem sabe entrergar um valor por vez
    next -> entregue-me o próximo valor
    iter -> entregue-me seu iterador
'''

# texto = 'Python'

# novoTexto = ''
# for letra in texto:
#     novoTexto += f'*{letra}'
#     print(letra)

# print(novoTexto)



# função range(início, fim, passo)

# numeros = range(0, 10, 2)  #  Indo do 0 ao 10 pulando de 2 em 2

# for numero in numeros:
#     print(numero)




#texto = iter('texto')  # __iter__()

#print(texto)
# print(texto.__next__())  #  entregando um elemento da variável "texto" por vez
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

#  outra maneira

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))



for i in range(1, 10):
    if i == 2:
        print('i é igual a 2, pulando...')
        continue
    
    if i == 8:
        print('i é igual a 8, seu else não será executado')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('for completo com sucesso!')
    






















