""" 
    Combinação -> Ordem não importa - iterável + tamanho do grupo, não repete valores
    
    Permutação -> Ordem importa

    Produto -> Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['João', 'Joana', 'Luiz', 'Letícia']

camisetas = [
    ['preta', 'branca'],
    ['p','m'],
    ['masculino', 'feminino']
]

def print_iter(iterator):
    print(*list(iterator), sep='\n')  
    print()

""" print_iter(combinations(pessoas,2))  # Mostrando uma combinação dos nomes da lista de 2 em 2 pessoas

print_iter(permutations(pessoas,2))  # Mostrando uma combinação dos nomes da lista de 2 em 2 pessoas importando a ordem, nesse caso a ordem alfabética """

print_iter(product(*camisetas))  # Mostra as combinações possíveis com os itens da lista 

