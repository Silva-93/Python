""" 
    Especifica os tipos de opbjetos a serem criados usando uma intâcia-protótipo e cria novos objetos pela cópia desse prótotipo

    Quais objetos são copiados com o sinal de atribuição?
        *
"""
from __future__ import annotations
from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'  # retorna o nome da classe e o que ela recebe


    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: list[Address] = []


    def add_address(self, address: Address) -> None:
        self.addresses.append(address)


    # Método que cria uma cópia dele mesmo
    def clone(self) -> Person:  
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':

    luiz = Person('Luiz', 'Miranda')
    endereco_luiz = Address('Av. Brasil', '250A')
    luiz.add_address(endereco_luiz)
    
    esposa_luiz = luiz.clone()
    esposa_luiz.firstname = 'Letícia'
    
    print(luiz)
    print(esposa_luiz)

    






























