'''
    *args - Argumentos não nomeados
    * - *args (empacotamento e despacotamento)

    O *args é muito usado quando você ainda não sabe a quantidade de parâmetros que serão passados na função. 

    **kwargs - Argumentos nomeados - retornam um dicionário
'''



# def soma(*args):
#     # é um acumulador, a cada iterção ele será somado com seu próprio valor mais o valor da iteração
#     total = 0  

#     for num in args:
#         total += num
#     return total

# soma_1_2_3 = soma(1,2,3)  # todos esses valores serão atribuídos ao args em forma de uma tupla
# print(soma_1_2_3)

# somaValores = soma(1,2,3,4,5,6,7,8,9)
# print(somaValores)

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# def multiplicar(*args):
#     totalMult = 1
#     for num in args:
#         totalMult *= num
#     return totalMult

# multi = multiplicar(10,10)
# print(multi)

# multi2 = multiplicar(2, 2, 2, 2, 2)
# print(multi2)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


# def par_impar(n):
#     numero = n % 2 == 0

#     if numero:
#         return f'O N° "{n}" é um número PAR'
#     else:
#         return f'O N° "{n}" é um número IMPAR'


# par = par_impar(2)
# print(par)

# impar = par_impar(5)
# print(impar)





pessoa = {
    'nome': 'Julia',
    'sobrenome': 'Feronato'
}

dados_passoa = {
    'idade': 23,
    'altura': 1.65
}



#  "extraindo" dicnionários | Desempacotamento de dicionários
pessoa_completa = {**pessoa, **dados_passoa}
# print(pessoa_completa)


def argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

# retorna um dicionpario
argumentos_nomeados(nome='Jouber', sobrenome='Vicente', idade=29, altura=1.75, peso=80)

print()

# desempacotando dicionário
argumentos_nomeados(**pessoa_completa)














