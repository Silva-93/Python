'''
    Forma rápida de criar listas a partir de iteráveis
'''

# criando uma lista com 10 números usando o for

# lista = []

# for numero in range(10):
#     lista.append(numero)
# print(lista)

# # mesma lista usando o list comprehension

# lista2 = [numero for numero in range(10)]

# print(lista2)

# # multiplicando os elementos da lista por 2
# lista3 = [numero*2 for numero in range(10)]
# print(lista3)



# Mapeamento de dados com list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

# criando um novo dicionário é almentando os preços em 5%
# novos_produtos = [{**produto, 'preco': produto['preco'] *1.05} for produto in produtos]
# print(*novos_produtos, sep='\n')


# print()


# criando um novo dicionário é almentando os preços em 5% se o valor do produto for maior que 20
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] *1.05} 
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos]

# print(*novos_produtos, sep='\n')



# # filtro de dados em list comprehension
# from pprint import pprint

# def p(v):
#     pprint(v, sort_dicts=False, width=40)



# Serão incluidos na lista os números menores que 4
# lista = [n for n in range(10) if n < 4]

# p(lista)


# novos_produtos = [
#     {**produto, 'preco': produto['preco'] *1.05} 
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if produto['preco'] > 10  # serão incluidos na lista os produtos com o preço maior que 10
# ]
# p(novos_produtos)







# list comprehension com mais de um for

