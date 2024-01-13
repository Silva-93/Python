""" 
    Chain of Responsibility (COR) é um padrão comportamental que tem a intenão de evitar o acoplamento do remetente de uma solicitação ao seu receptor, ao dar a mais de um objeto a oportunidade de tratar a solicitação. Encadear os objetos receptores passando a solicitação ao longo da cadeia até que um objeto a trate.  
"""
from __future__ import annotations
from abc import ABC, abstractmethod

 
# handler (manipulador)
class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor


    def handle(self, letter: str) -> str:
        resp_handlerABC = f'HandlerABC: Conseguiu tratar o valor {letter}'

        if letter in self.letters:
            return resp_handlerABC 
        
        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['D', 'E', 'F']
        self.sucessor = sucessor


    def handle(self, letter: str) -> str:
        resp_handlerDEF = f'HandlerDEF: Conseguiu tratar o valor {letter}'

        if letter in self.letters:
            return resp_handlerDEF 
        
        return self.sucessor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'HandlerUnsolved: Não conseguiu trar {letter}'





if __name__ == '__main__':
    handler_Unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_Unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))
    print(handler_abc.handle('I'))















