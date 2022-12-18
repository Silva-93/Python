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
lista = [10, 20, 30, 40]

lista[2] = 300  #  Alterando o valor do 3° elemento
print(lista)


#  Apagando um valor especifico da lista
del lista[2]
print(lista)


#  Adicionando elementos na lista
lista.append(50)
print(lista)


#  Removendo o último elemento da lista, caso não seja indicado qual índice é para ser excluído, o pop() excluirá o elemento no último índice da lista
lista.pop()
print(lista)


#  Inserindo elementos em um índice específico da lista, caso não seja indicado qual índice é para ser inserido, o insert() adicionará o elemento no último índice da lista
lista.insert(2, 30)
print(lista)



#  Limpando a lista, o clean() limpa todos os elementos da lista deixando uma lista vazia
lista.clear()
print(lista)


#  juntando 2 ou mais listas em uma só
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
print(lista_c)

# outra maneira

lista_a.extend(lista_b)
print(lista_a)






