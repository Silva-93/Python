# Implementando o protocolo do Iterator em python

from collections.abc import Sequence
from typing import Iterator


class MyList(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0
        self._next_index = 0
    

    # método para adicionar um valor na lista
    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1


    # método para saber o tamanho da lista
    def __len__(self):
        return self._index


    # método o index da lista
    def __getitem__(self, index):
        return self._data[index]
    
    
    # método que permite configurar um valor (reatribuir um valor)
    def __setitem__(self, index, value):
        self._data[index] = value


    # método que implementa um iterator próprio
    def __iter__(self):
        return self
    

    # método que retorna o próximo valor da lista
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        
        value = self._data[self._next_index]
        self._next_index += 1
        return value



if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria')
    lista.append('João', 'helena', 'Maria')
    lista[0] = 'Marta'

    # print(lista._data)

    for item in lista:
        print(item)





























