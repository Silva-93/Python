""" 
    dataclasses

    O módulo dataclasses fornece um decorador e funções para criar métodos como __init__(), __repr__(), __eq__(), entre outros, em classes definidas pelo usuário.
    Em resumo, dataclasses são syntax sugar para criar classes normais.
"""


from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int



if __name__ == '__main__':
    p1 = Pessoa('jouber', 30)
    p2 = Pessoa('ana', 21)
    
    print(p1)
    print(p1 == p2)


































