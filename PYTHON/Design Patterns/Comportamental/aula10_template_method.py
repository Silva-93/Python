""" 
    Tempate Method tem a intenção de definir um algoritmo em um método, postergando alguns passos para as subclasses por herança. Template method permite que subclasses redefinam certos passos de um algorítimo sem mudar a estrutura do mesmo.

    Também é possível definir hooks para que as subclasses utilizem caso necessário.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


# classe abstrata
class Pizza(ABC):
    def prepare(self) -> None:
        """ Template method """ 
        self.add_ingrentientes()  # Abstract
        self.cook()  # Abstract
        self.cut()  # Concreto dentro da classe abstrata
        self.server()  # Concreto dentro da classe abstrata


    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando pizza.')


    def server(self) -> None:
        print(f'{self.__class__.__name__}: servindo a pizza.')


    @abstractmethod
    def add_ingrentientes(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class AModa(Pizza):
    def add_ingrentientes(self) -> None: 
        print(f'{self.__class__.__name__}: presunto, queijo, goiabada')

    
    def cook(self) -> None: 
        print(f'{self.__class__.__name__}: cozinhando por 45min no forno a lenha')


if __name__ == '__main__':
    a_moda = AModa()
    a_moda.prepare()

