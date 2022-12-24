'''
    Tipo list
    Suporta vários valores de tipos diferentes ao mesmo tempo
    Conhecimento reotilizáveis - índices e fatiamento
    Métodos úteis - appen(), insert(), pop(), del(), clear(), extend()... 

    Create, Read, Update, Delete -> CRUD
'''

#  formas de criar uma lista

#lista = []
# ou 
#lista2 = list()


#  Acessando os elementos da lista

# lista =[123, True, 'texto', 1.2, []]

# print(lista[0])  #  1° elemento da lista
# print(lista[1])  #  2° elemento da lista
# print(lista[2])  #  3° elemento da lista 
# print(lista[3])  #  4° elemento da lista 
# print(lista[4])  #  5° elemento da lista 


#  Alterando valores de uma lista
# lista = [10, 20, 30, 40]

# lista[2] = 300  #  Alterando o valor do 3° elemento
# print(lista)


# #  Apagando um valor especifico da lista
# del lista[2]
# print(lista)


# #  Adicionando elementos na lista
# lista.append(50)
# print(lista)


# #  Removendo o último elemento da lista, caso não seja indicado qual índice é para ser excluído, o pop() excluirá o elemento no último índice da lista
# lista.pop()
# print(lista)


# #  Inserindo elementos em um índice específico da lista, caso não seja indicado qual índice é para ser inserido, o insert() adicionará o elemento no último índice da lista
# lista.insert(2, 30)
# print(lista)



# #  Limpando a lista, o clean() limpa todos os elementos da lista deixando uma lista vazia
# lista.clear()
# print(lista)


# #  juntando 2 ou mais listas em uma só
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]

# lista_c = lista_a + lista_b
# print(lista_c)

# # outra maneira

# lista_a.extend(lista_b)
# print(lista_a)


# #  copiando uma lista
# lista_d = [7, 8, 9]

# lista_e = lista_d.copy()
# print(lista_e)


#  exibindo os índices da lista
# lista_nome = ['Maria', 'João', 'Ana', 'Rafael']
# indices = range(len(lista_nome))

# for i in indices:
#     print(i, lista_nome[i])

# outra maneira

# listaNome = ['Joao', 'Maria', 'Luiza', 'Fernando']
# #                             fazendo com que a contagem comece do 1
# for i in enumerate(listaNome, start=1):
#     print(i)



#  Exercício listas
'''
    Faça uma lista de compra com uma lista. O usuário deve ter a possibilidade de inserir, apagar e listar os valores da lista. Não permita que o programa quebre com erros de índice inexistentes da lista.
'''



import os

lista = []
while True:
    # O usuário deve ter a possibilidade de inserir, apagar
    print('Selecione uma opção. Digite [f]im para sair do programa.')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')  # limpa o terminal
        item = input('Item: ')
        lista.append(item)


    # Apagar itens da lista 
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]  #  apaga um item da lista
        except:
            print('Não foi possível apragar esse índice.')


    #  Listar itens da lista
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, item in enumerate(lista):  # lista a os itens da lista com seus índices
            print(f'Índice [{i}] -> {item}')

    elif opcao == 'f':
        print('Finalizando o programa')
        break


    else:
        print('Por favor, escolha entre as opções [i], [a] ou [l].')




















