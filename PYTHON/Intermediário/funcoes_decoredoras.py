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

@decoradora
def soma(x, y):
    return x + y 


dez_mais_cindo = soma(10, 5)

print(dez_mais_cindo)











