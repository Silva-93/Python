""" 
    dataclasses

    O módulo dataclasses fornece um decorador e funções para criar métodos como __init__(), __repr__(), __eq__(), entre outros, em classes definidas pelo usuário.
    Em resumo, dataclasses são syntax sugar para criar classes normais.

    É possível definir valores padrão para valores imutáveis
"""


from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    nome: str = field(default='MISSING')
    sobrenome: str = 'Not sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)  # tornando a lista como um valor padrão



if __name__ == '__main__':
    p1 = Pessoa()

    print(p1)