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
def mostre():
    print('Isso é uma função sem parâmetro')
    print('Posso ter quantos prints eu quiser')
    print('que para exibilos todos de uma vez')
    print('Só preciso chamar a função uma vez.')

# chamando a função
mostre()



# Função com parâmetros
def soma(a, b):
    return f'A soma de {a} + {b} é igual a: {a+b}'

# chama a função com parâmetro
print(soma(15, 15))


# Chamando a função com argumentos nomeados
print(soma(a=10, b=20))



# Função com parâmetros e valores padrãos 
def multiplicacao(a=10, b=10):
    return a * b

# Quanda valores padrões nas funções, caso não queira alterar esses valores, a função pode ser chamada sem a necessidade de passar parâmetros
print(multiplicacao())
print(multiplicacao(5, 5))


# Sabendo quando um parâmetro de valor "None" foi passada nos argumentos
def multi(x, y, z=None):
    if z is not None:
        return f'{x= } {y= } {z= } | R= {x*y*z}'
    else:
        return f'{x= } {y= } | R= {x*y}'

print(multi(2, 5, 3))

print(multi(2, 3))
    






























