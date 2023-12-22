""" 
    dataclasses

    O módulo dataclasses fornece um decorador e funções para criar métodos como __init__(), __repr__(), __eq__(), entre outros, em classes definidas pelo usuário.
    Em resumo, dataclasses são syntax sugar para criar classes normais.

    __post_init__() -> é executado logo após a dataclasse
"""


from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'



if __name__ == '__main__':
    p1 = Pessoa('jouber', 'vicente')

    print(p1)
    print(p1.nome_completo)