"""
    Variáveis são valores armazenados na memória para serem usados postariormente em outras partes do código.
    sintaxe.
    name = value | O sinal de "=" é usada para atribuir um valor a variável, esse valor pode ser de qualquer tipo 

    exemplos.:
    nome = 'Jouber'
    idade = 29
    altura = 1.75
    ... 
"""

# frase = 'Uma mente que se abre a uma nova ideia jamais voltará ao seu temanho original.'

# numero1 = 10
# numero2 = 20
# soma = numero1 + numero2

# print(frase)
# print(numero1)
# print(numero2)
# print(soma)

# #  Exercício

# nome = 'Jouber'
# sobrenome = 'Vicente'
# idade = 29
# altura = 1.75
# ano_nascimento = 2022 - idade
# maior_de_idade = idade >= 18

# print(f'Nome: {nome}')
# print(f'Sobrenome: {sobrenome}')
# print(f'Idade: {idade}')
# print(f'Ano de nascimento: {ano_nascimento}')
# print(f'É maior de idade: {maior_de_idade}')
# print(f'Altura em metros: {altura}m')



'''
    CONSTANTE = variáveis que não mudam de valor
    Muitas condições no mesmo if (ruim)

    Quando se quer criar uma variável constante, a variável é feita com todas as letras maiúsculas

'''

velocidade = 61

km = 90

RADAR_1 = 60  #  Velocidade máxima do redar 1
LOCAL_1 = 100  #  Local onde o radar 1 está
RADAR_RANGE = 1  #  A distância onde radar pega


# if velocidade > RADAR_1:
#     print('Velocidade carro passo do radar 1')


# if  km >= (LOCAL_1 - RADAR_RANGE) and km <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
#     print('Carro multado no radar 1')


#  OUTRA MANEIRA DE FAZER 

val_carro_pass_radar1 = velocidade > RADAR_1

carro_multado_radar1 = km >= (LOCAL_1 - RADAR_RANGE) and km <= (LOCAL_1 + RADAR_RANGE)

if val_carro_pass_radar1:
    print('Velocidade carro passo do radar 1')

if carro_multado_radar1:
    print('Carro multado no radar 1')





