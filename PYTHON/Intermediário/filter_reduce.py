# filter é um filtro funcional

""" def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print_iter(produtos)

# filtrando os produtos com o preço maior que 10
novo_produto = filter(lambda produto: produto['preco'] > 10, produtos)

# outra maneira
novos_procutos = [produto for produto in produtos if produto['preco'] > 10]

print_iter(novo_produto) """




# --------- reduce --------- # 

# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Obtendo o valor total dos produtos
#total = 0
""" for produto in produtos:
    total += produto['preco']  # somando os preços.

print(f'{total:.2f}') """

# Usando list comprehension
""" total = ''
print(sum([produto['preco'] for produto in produtos])) """
 

# Usando o "REDUCE"

""" def funcao_reduce(acumulador, produto):
    return acumulador + produto['preco']

total = reduce(
    funcao_reduce,
    produtos,
    0  #  valor inicial
)

print(total) """


# Usando "REDUCE" com função lambda

total = reduce(lambda acumuldor, produto: acumuldor + produto['preco'],
               produtos,
               0)  # o 0 é o valor inícial

print(f'{total:.2f}')