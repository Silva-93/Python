'''
Considerando duas listas de interiros ou floats (lista A e lista B).
Some os valores nas listas retornando uma nova lista com os valores somados.

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a =   [1, 2, 3, 4, 5, 6, 7]
lista_b =   [1, 2, 3, 4]

--------- resultado ---------
lista_soma =    [2, 4, 6, 8]

'''

# Listas 
lista_a =   [1, 2, 3, 4, 5, 6, 7]
lista_b =   [1, 2, 3, 4]


# 1° maneira de resolução
""" lista_soma = []

for i in range(len(lista_b)):  # Pegando os índices da lista
    lista_soma.append(lista_a[i] + lista_b[i])  # Somando os somando os índices correspondentes das listas

print(lista_soma)
 """

# 2° maneira de resolução
""" lista_soma = []

for i, _ in enumerate(lista_b):  # Pegando os índices da lista
    lista_soma.append(lista_a[i] + lista_b[i])  # Somando os somando os índices correspondentes das listas
print(lista_soma) """

# 3° maneira de resolução
""" lista_soma = [x + y for x, y in zip(lista_a, lista_b)]  # zip -> união das duas listas. zip só une as listas até o tamanho da menor lista
print(lista_soma) """


# 4° maneira de resolção
from itertools import zip_longest
 
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [2, 4, 6, 8, 5, 6, 7]

""" 
utilisando o "fillvalue" como 0 (zero), assim conseguimos capturar os valores restantes da lista maior, realizando contas, sem obter um erro em nosso programa.
"""