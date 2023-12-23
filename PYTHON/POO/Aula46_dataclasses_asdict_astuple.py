""" 
    dataclasses

    O módulo dataclasses fornece um decorador e funções para criar métodos como __init__(), __repr__(), __eq__(), entre outros, em classes definidas pelo usuário.
    Em resumo, dataclasses são syntax sugar para criar classes normais.

    __post_init__() -> é executado logo após a dataclasse

    asdict(cls)  -> converte a classe em um dicionário
    astuple(cls)  -> converte a classe em uma tupla
"""


from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'



if __name__ == '__main__':
    p1 = Pessoa('jouber', 'vicente')

    print(asdict(p1))  # converte a classe em um dicionário
    print(astuple(p1))  # converte a classe em uma tupla
    