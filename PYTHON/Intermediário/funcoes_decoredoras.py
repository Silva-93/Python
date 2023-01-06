'''
    Funções decoradoras e decoradores
    
    Decorar = Adicionar / Remover / Restringir / Alterar

    Funções decoradores são funções que decoram outras funções, decoradores são usados para fazer o python usar as funções decoradoras em outras funções

    Caso uma função seja decorada por uma função decoradora, imediatamente o python executa a função decoradora
'''

# def criar_funcao(func):
#     def interna(*args, **kwargs):
#         print('Função será decorada')
#         for arg in args:
#             e_str(arg)
#         resultado = func(*args, **kwargs)
#         print('Função foi decorada')
#         return resultado
#     return interna


# def e_str(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma string.')


# @criar_funcao  # Decurador
# def inverte_string(string):
#     return string[::-1]


# str_invertida = inverte_string('Jouber')
# print(str_invertida)



# Decoradores com parâmetros


def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

# @decoradora
def soma(x, y):
    return x + y 


# dez_mais_cindo = soma(10, 5)

# print(dez_mais_cindo)



# Ordem dos decoradoes

def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


# @parametros_decorador(nome='quinto')
# @parametros_decorador(nome='quarto')
# @parametros_decorador(nome='terceiro')
# @parametros_decorador(nome='segundo')
# @parametros_decorador(nome='primeiro')
# def soma(x, y):
#     return x + y


# cinco_mais_dez = soma(5, 10)

# print(cinco_mais_dez)




# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]




# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [(lista1[i], lista2[i]) for i in range(intervalo_maximo)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(l1, l2))

# Outra maneira
print(list(zip(l1, l2)))

from itertools import zip_longest 
# Usa a lista maior
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))


# Exercício
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""



