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



while True:
    n1 = input('Digite um número.\nNúmero: ')
    n2 = input('Digite outro número.\nNúmero: ')
    operador = input('Digite o operador para realizar a conta. [+ - / *].\nOperador: ')

    numerosValidos = None

    numero1 = 0
    numero2 = 0
    
    try:
        #  Convertendo para números float
        numero1 = float(n1)
        numero2 = float(n2)

        #  Validando se são números válidos
        numerosValidos = True    
    except:
        numerosValidos = None

    if numerosValidos is None:
        print('Há um ou mais números inválidos digitados.')
        continue

    operadoresPermitidos = '+-/*'


    if operador not in operadoresPermitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando a sua conta. Confira o resultado abaixo.')
    if operador == '+':
        print(f'O resultado de {numero1} + {numero2} é {numero1 + numero2}')

    elif operador == '-':
        print(f'O resultado de {numero1} - {numero2} é {numero1 - numero2}')

    elif operador == '/':
        print(f'O resultado de {numero1} / {numero2} é {numero1 / numero2}')

    elif operador == '*':
        print(f'O resultado de {numero1} * {numero2} é {numero1 * numero2}')
    
    else:
        print('Tem algo de errado. Tente novamente.')

    
    sair = input('Quer sair? [s]air: ')
    #  deixar as letras em minúsculo e verifica se começa com 's'
    sair = sair.lower().startswith('s')

    if sair is True:
        break
















