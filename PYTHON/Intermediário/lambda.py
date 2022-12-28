# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista = [4,32,1, 34, 5, 6, 6,21]

# lista.sort()  # ordina a lista de forma crescente
# print(lista)
# O ".sort()" altera a ordem da lista

# O "sorted()" cria uma cópia rasa da lista e muda a ordem da cópia


# lista.sort(reverse=True)  # ordina a lista de forma decrescente
# print(lista)


# Essa função ordena os dicionários pelos nomes na ordem alfabética
# def ordena(item):  
#     return item['nome']

# lista.sort(key=ordena)

# for item in lista:
#     print(item)


# outra maneira de executar essa função com função lambda



# l1 = sorted( lista, key=lambda item: item['nome'])

# for item in l1:
#     print(item)



# função criada para executar as funções lambdas (boa prática de programação)
def executa(funcao, *args):
    return funcao(*args)




def soma(x, y):
    return x + y

# Mesma função usando função lambda
print(executa(lambda x, y: x + y, 2, 3))
# executando a função "executa"   parâmetros da função lambda                                      


def multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# Mesma função usando função lambda
duplica = executa(lambda m: lambda n: n*m, 2)

print(duplica(3))































