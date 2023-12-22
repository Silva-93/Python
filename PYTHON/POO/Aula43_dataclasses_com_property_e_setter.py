""" 
    dataclasses

    O módulo dataclasses fornece um decorador e funções para criar métodos como __init__(), __repr__(), __eq__(), entre outros, em classes definidas pelo usuário.
    Em resumo, dataclasses são syntax sugar para criar classes normais.
"""


from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)




if __name__ == '__main__':
    p1 = Pessoa('jouber', 'vicente')
    p1.nome_completo = 'Joana Dark Almeida'

    print(p1)
    print(p1.nome_completo)