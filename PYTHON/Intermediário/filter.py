# filter é um filtro funcional

def print_iter(iterador):
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
""" novos_procutos = [produto for produto in produtos if produto['preco'] > 10] """

print_iter(novo_produto)