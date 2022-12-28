
# set - Conjuntos em python (tipo set).
# sets são mutáveis porém, só aceitam tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1,2,3,4}
s1 = set('Isso é um set') 
print(s1, type(s1))

s2 = {'Isso também é um set'} 
print(s2, type(s2))

# para criar um set vazio é necessário usar a classe set()
s3 = set()  # set vazio

# Sets são eficientes para remover valores duplicados de iteráveis.
s4 = {1,2,3,3,3,3,3,3,3,4,1,5,6,2}  # os sets tiram os valores repetidos "naturalmente"
print(s4)

# Sets não tem índixes
# Sets não garantem a ordem dos elementos
# Sets são iteráveis for, in, not in

for num in s4:
    print(num)

# métodos úteis
# add, update, clear, discard
s5 = set()
s5.add('nome')  # adcionandoum valor no set o ".add()" só aceita um valor por vez 
s5.add('1')
print(s5)

s5.update('iterado')  #similar ao ".add" mas quando for inserido o valor, ele irá para o set de forma iterada 'i', 't', 'e'..., para mandar valores sem estar de forma iterada, mando o valor como uma tupla ou lista
s5.update(('Não_iterado',1,2,3,4))
print(s5)

# s5.clear()  #  limpa todos os valores do set, deixando um set vazio

s5.discard('Não_iterado')  # elimina o valor passado
print(s5)

# Operadores úteis com sets

# união | união (unio) -> Une
# Intersecção & (intersection) -> Itens peresentes em ambos os conjustos
# Diferença - -> Itens presentes apenas no set da esquerda
# Diferênça simétrica ^ -> Itens que não estão nos conjuntos


s6 = {1,2,3}
s7 = {2,3,4}

s8 = s6 | s7  # unindo os sets
print(s8)

s9 = s6 & s7  # Junta os valores que existem nos 2 sets
print(s9)



s10 = s6 - s7  # Mostra os valores que exitem somente no set da esquerda, nesse caso do s6
print(s10)


s11 = s6 ^ s7  # Mostra os valores únicos de cada set, valores que só estão em apenas um set
print(s11)



# Exercício "set()"



"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]



def encontraDuplicado(lista_de_numeros):
    numerosChecados = set()
    primeiroDuplicado = 'Não há duplicados.' # valor que será retornado se não tiver n° deplicados
    
    for numero in lista_de_numeros:
        if numero in numerosChecados:  # verifica se o n° já está adicionado
            primeiroDuplicado = numero  # caso já esteja adicionado o ele será o n° que está duplicado
            break

        numerosChecados.add(numero)  # adiciono número no set() vazio
    
    print()
    print()

    return primeiroDuplicado

for lista in lista_de_listas_de_inteiros:
    print(lista, encontraDuplicado(lista))





























