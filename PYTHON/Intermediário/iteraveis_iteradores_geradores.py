'''
    Iterável - Tem valores sequências

    Iterador - Fornece uma maneira de acessar sequencialmente os elementos de um objeto agregado sem expor sua representação subjacente. Fornece um único valor
'''

iteravel = ['eu', 'tenho', '__iter__']

iterador = iter(iteravel)

# print(next(iterador))  # retorna: eu
# print(next(iterador))  # retorna: tenho
# print(next(iterador))  # retorna: __iter__


# Generator -> São funções que sabem pausar, todo generetor também é um iterator, mas um iterator não é um generator

#criando uma generator expression
lista_generator = [n for n in range(100)]  # Numa lista, seu tamanho é salvo na memória por inteiro assim que é criada e executada.

generator = (n for n in range(100))  # O generator não salva todos os valores na memória, ele só entrega um valor por vez.  
print(generator)
# # obtando os valore do generator
# print(next(generator))  # É preciso um "next" para cada valor do generator
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


# criando uma função com generator

def generator(n=0):
    yield 1  # Pausa a função e guarda o valor em um "next"
    return "Acabou!"

gen = generator(n=0)
print(next(gen))


#outra função


def generator2(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return

gen2 = generator2()

for num in gen2:
    print(num)

