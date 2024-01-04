""" 
    O singleton tem a intenção de garantir que o estado do objeto seja igual para todas as instâncias.
"""

class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'  # retorna o nome da classe e o que ela recebe


    def __repr__(self) -> str:
        return self.__str__()


class MonostateSimple(StringReprMixin):
    _state: dict = {
        'X': 10,
        'Y': 20,
    }

    def __init__(self, nome=None, sobrenome=None) -> None:
        self.__dict__ = self._state
        
        if nome != None:
            self.nome = nome
        
        if sobrenome != None:
            self.sobrenome = sobrenome


if __name__ == '__main__':
    m1 = MonostateSimple('Jouber', 'Vicente')
    m2 = MonostateSimple()
    print(m1)


















