""" 
    GoF - Memento é um padrão de projeto comportamental que tem a intenção de permitir que você salve e restaure um estado anterior de um objeto originator sem revelar os detalhes da sua implementação e sem violar o encapsulamento.

    Originator é o objeto que deseja salvar seu estado.
    Memento é usado para salvar o estado do originator.
    Caretaker é usado para armazenar mementos.
    Caretaker também é usado com o Padrão Command
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any


class Memento:
    def __init__(self, state: dict) -> None:
        self._state: dict
        super().__setattr__('_state', state)


    def get_state(self) -> dict:
        return self._state


    # método imutável
    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError('Sorry, i am immutable.')


class ImageEditor:
    # estado
    def __init__(self, name:str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height


    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))  # __dict__ é namespace dessa classe (ImageEditor), todos os atributos da classe vão estar dentro do __dict__


    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()    


    def __str__(self) -> str:
        return f'{self.__class__.__name__}  ({self.__dict__})'


class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: list[Memento] = []


    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())


    def restore(self) -> None:
        if not self._mementos:
            return
        
        self._originator.restore(self._mementos.pop())





if __name__ == "__main__":
    img = ImageEditor('FOTO_1.jpg', 111, 111)
    caretaker = Caretaker(img)

    caretaker.backup()

    # editando a imagem
    img.name, img.width, img.height = 'FOTO_2.jpg', 222, 222
    caretaker.backup()

    img.name, img.width, img.height = 'FOTO_3.jpg', 333, 333
    caretaker.backup()

    img.name, img.width, img.height = 'FOTO_4.jpg', 444, 444
    # caretaker.backup()

    caretaker.restore()  # retorna ao 333
    caretaker.restore()  # retorna ao 222
    caretaker.restore()  # retorna ao 111
    caretaker.restore()  # permanece no 111

    print(img)