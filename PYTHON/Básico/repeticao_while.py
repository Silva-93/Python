'''
    While (enquanto)

    Executa uma ação enquanto ela for verdadeira.
'''


# contador = 0

# while contador < 100:
#     contador += 1
#     print(contador)

#     if contador == 10:
#         print('Chegou no 10!')
#         continue

#     if contador == 20:
#         print('Chegou no 20!')
#         break

# print('Acabou!')


# qtd_linha = 5

# qtd_coluna = 5

# linha = 1

# while linha <= qtd_linha:
#     coluna = 1
    
#     while coluna <= qtd_coluna:

#         print(f'{linha=}   ->   {coluna=}')

#         coluna += 1
    
#     linha +=1


# print('Acabou!')




# nome = 'Jouber Vicente'

# indice = 0 

# novo_nome = ''
# while indice < len(nome):
#     #  percorrendo o texto digitado na variável nome
#     letra = nome[indice]  #  "pegando" as letras da str
    
#     novo_nome += f'*{letra}'  #  Adicionando as letras em "novo_nome"
#     indice += 1

# print(novo_nome)



#  CALCULADORA COM WHILE



# while True:
#     n1 = input('Digite um número.\nNúmero: ')
#     n2 = input('Digite outro número.\nNúmero: ')
#     operador = input('Digite o operador para realizar a conta. [+ - / *].\nOperador: ')

#     numerosValidos = None

#     numero1 = 0
#     numero2 = 0

#     try:
#         #  Convertendo para números float
#         numero1 = float(n1)
#         numero2 = float(n2)

#         #  Validando se são números válidos
#         numerosValidos = True    
#     except:
#         numerosValidos = None

#     if numerosValidos is None:
#         print('Há um ou mais números inválidos digitados.')
#         continue

#     operadoresPermitidos = '+-/*'


#     if operador not in operadoresPermitidos:
#         print('Operador inválido.')
#         continue

#     if len(operador) > 1:
#         print('Digite apenas um operador.')
#         continue
    
#     print('Realizando a sua conta. Confira o resultado abaixo.')
#     if operador == '+':
#         print(f'O resultado de {numero1} + {numero2} é {numero1 + numero2}')

#     elif operador == '-':
#         print(f'O resultado de {numero1} - {numero2} é {numero1 - numero2}')

#     elif operador == '/':
#         print(f'O resultado de {numero1} / {numero2} é {numero1 / numero2}')

#     elif operador == '*':
#         print(f'O resultado de {numero1} * {numero2} é {numero1 * numero2}')
    
#     else:
#         print('Tem algo de errado. Tente novamente.')

    
#     sair = input('Quer sair? [s]air: ')
#     #  deixar as letras em minúsculo e verifica se começa com 's'
#     sair = sair.lower().startswith('s')

#     if sair is True:
#         break





# EXERCÍCIO -> QUAL LETRA FOI MAIS REPETIDA.


frase = 'Python é uma liguangem multiparadigma criada por Guido Van Rossum.'

i = 0
qtd_de_vezes_letra_apareceu = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    
    letra_atual = frase[i]  #  Percorrendo cada letra da frase
    
    if letra_atual == ' ':
        i += 1
        continue

    qtd_de_letras = frase.count(letra_atual)  #  contando a quantidade que as letras apareceream
    
    if qtd_de_vezes_letra_apareceu < qtd_de_letras:
        qtd_de_vezes_letra_apareceu = qtd_de_letras
        letra_apareceu_mais_vezes = letra_atual
    
    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}" que apareceu {qtd_de_vezes_letra_apareceu}x')



#  Exercício
'''
    Faça um jogo para o usuário adivinhar a palavra secreta.
    Você vai propor uma palavra secreta qualquer e vaidar a 
    possibilidade do usuário digitar apenas uma letra.

    Quando o usuário digitar a letra você var conferir se a 
    letra está dentro da paralavra secreta.

    Se a letra digitada estiver na palavra secreta, exiba a letra

    Se a letra não estiver na palavra secreta, exiba *

    Faça uma contagem das tentativas do usuário.
'''


palavra_secreta = 'secreta'
letras_acertadas = ''
numero_tentativas = 0


while True:
    letra_digitada = input('Digite uma letra para adivinha a palavra secreta.\nLetra: ')
    numero_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada  # armazenando as letras acertadas

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'
    

    print(f'Palavra formada: "{palavra_formada}"')


    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU! PARABÉNS!')
        print(f'A palavra era "{palavra_secreta}"')
        print(f'O número de tentativas foram {numero_tentativas}')
        break




