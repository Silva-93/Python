'''
    Introdução às funções (def) em Python
    Funções são trechos de códigos usados para 
    replicar determinada ação ao longo do seu
    código. Elas podem receber valores para parâmetros (argumentos)
    e retornar um valor específico.
    Por padrão as funções em Python retornam o valor "None".

    Sintaxe para criar uma função

    def <nome>():
        metodos

    def <nome>(parâmetros):
        metodos
'''


# Função sem parâmetro
# def mostre():
#     print('Isso é uma função sem parâmetro')
#     print('Posso ter quantos prints eu quiser')
#     print('que para exibilos todos de uma vez')
#     print('Só preciso chamar a função uma vez.')

# # chamando a função
# mostre()



# # Função com parâmetros
# def soma(a, b):
#     return f'A soma de {a} + {b} é igual a: {a+b}'

# # chama a função com parâmetro
# print(soma(15, 15))


# # Chamando a função com argumentos nomeados
# print(soma(a=10, b=20))



# # Função com parâmetros e valores padrãos 
# def multiplicacao(a=10, b=10):
#     return a * b

# # Quanda valores padrões nas funções, caso não queira alterar esses valores, a função pode ser chamada sem a necessidade de passar parâmetros
# print(multiplicacao())
# print(multiplicacao(5, 5))


# # Sabendo quando um parâmetro de valor "None" foi passada nos argumentos
# def multi(x, y, z=None):
#     if z is not None:
#         return f'{x= } {y= } {z= } | R= {x*y*z}'
#     else:
#         return f'{x= } {y= } | R= {x*y}'

# print(multi(2, 5, 3))

# print(multi(2, 3))
    



#  Exercício funções

'''
    Crie funções que duplicam, triplical e quadruplicam o número recebido como parâmetro
'''

# def duplicar(n):
#     duplicar_n = n * 2
#     return f'O dobru de "{n}" é "{duplicar_n}"'

# def triplicar(n):
#     triplicar_n = n * 3
#     return f'O triplu de "{n}" é "{triplicar_n}"'


# def quadrupilar(n):
#     quadrupilar_n = n * 4
#     return f'O quadruplo de "{n}" é "{quadrupilar_n}"'


# dobro = duplicar(2)

# triplo = triplicar(3)

# quadruplo = quadrupilar(4)

# print(dobro)
# print(triplo)
# print(quadruplo)

# Outra maneira de resover o mesmo exercício

def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


dobro = multiplicador(2)  #  número que será o multiplicador

triplo = multiplicador(3)

quadruplo = multiplicador(4)


print(dobro(2))  #  número que será multiplicado

print(triplo(3))

print(quadruplo(4))






