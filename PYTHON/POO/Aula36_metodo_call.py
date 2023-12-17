""" 
    Método especial __call__

    O método __call__ torna a instância da classe executável

    callable é algo que pode ser executado com parênteses
    
    Em classes normais, __call__ faz a instância de uma classe "callable"
"""


from typing import Any


class Callme:
    def __init__(self, phone) -> None:
        self.phone = phone


    def __call__(self, name):
        print(f'{name} está ligando para: {self.phone}')


call1 = Callme('9 9799 5032')
call1('Jouber')