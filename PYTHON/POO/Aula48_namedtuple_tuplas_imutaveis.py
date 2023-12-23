""" 
    namedtuples - tuplas imutáveis com nomes para valores.
    Usamos namedtuples para criar classes de objetos que são apenas um agrupamento de atributos, como classes normais sem métodos, ou registros de bases de dados, etc.
    As namedtuples são imutáveis assim como as tuplas.
"""

from collections import namedtuple



Carta = namedtuple('Carta', ['valor', 'naipe'])  # criando uma classe

as_espadas = Carta('A', '♠️')

print(as_espadas)
print(as_espadas.valor)
print(as_espadas.naipe)
print(as_espadas._fields)

print('---------------')

for valor in as_espadas:
    print(valor)


































