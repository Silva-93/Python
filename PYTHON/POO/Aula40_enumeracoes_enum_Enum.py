""" 
    Enum -> Enumerações

    Enumerações na programação, são usadas em ocasiões onde temos um determinado número de coisas. Enums têm menbros e sues valores são constantes.

    Enums em python:
        - São um conjunto de nomes simbólicos (membros) ligados a valores únicos, podem ser iterados para retornar seus menbros canônicos no ordem de definição

    enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada diretamente (mesmo assim, Rnums não são classes normais um Python).
    Você poderá usar seu Enum com type annotations, com isintances e outras coisas relacionadas com tipo.

    Para obter os dados:
        Membro = Classe(valor), Classe['chave']
        chave = Classe.chave.name
        valor = Classe.chave.value
"""

import enum
#                                      1          2
# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])


class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2
    CIMA = enum.auto()  # gera a enumeração automaticamente
    BAIXO = enum.auto()



def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')


    print(f'Movendo para {direcao.name} ({direcao.value})')



mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.CIMA)
mover(Direcoes.BAIXO)