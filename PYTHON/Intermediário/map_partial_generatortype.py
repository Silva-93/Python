# map - para mapear dados
from functools import partial

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

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

#  variável que aumenta em 10%
aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

#  aumentado os valores em 10%
""" novos_precos = [{**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos] """

def muda_preco(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

novos_precos = map(
    muda_preco, produtos
)

print_iter(novos_precos)