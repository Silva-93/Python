# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
from dados import produtos
import copy

copia_produtos = copy.deepcopy(produtos)

novos_produtos = [
    
    {**produto, 'preco': round(produto['preco'] * 1.1,2)} 
    for produto in copia_produtos
]

# print(*produtos, sep='\n')
# print('-'*40)
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copia_produtos,
    key=lambda produto: produto['nome'], reverse=True
)
# print(*produtos, sep='\n')
# print('-'*40)
# print(*produtos_ordenados_por_nome, sep='\n')



# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copia_produtos,
    key=lambda produto: produto['preco'],  
)
print(*produtos, sep='\n')
print('-'*40)
print(*produtos_ordenados_por_preco, sep='\n')