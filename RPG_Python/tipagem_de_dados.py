from collections.abc import Callable
from typing import TypeVar

# Anotações básicas em variáveis
uma_string: str = 'Um valot'
uma_inteiro: int = 1234
uma_float: float = 1.345
uma_boolean: bool = True
uma_set: set = {1, 5, 63}
uma_lista: list = []
uma_tupla: tuple = ()
uma_dicionatio: dict = {}


# tipagem em funções
def soma(x: int, y: int, z: float) -> float:
    return x + y + z


 # tipagem em listas
lista_inteiros: list[int] = [1, 2, 3, 4, 5]
lista_strings: list[str] = ['a', 'b', 'c']
lista_tuplas: list[tuple] = [(1, 'a'), (2, 'b')]
lista_listas_int: list[list[int]] = [[1], [1, 3, 5]]


# tipagem em dicionários
um_dict: dict[str, int] = {
    'A': 1,
    'B': 2,
    'C': 3
}

um_dict_de_listas: dict[str, list[int]] = {
    'A': [1, 2],
    'B': [3, 4],
    'C': [5, 6],
}

# type alias -> Adicionar tipos a variáveis
ListaInteiros = list[int]  # Alias do tipo
DictListaIneiros = dict[str, ListaInteiros]


# Unindo dois tipos de dados
str_e_int: str | int = 1

lista_de_int_ou_str: list[int | str] = [1, 2, 'a', 'b']


# tipando valores "opcionais"
def mult(x:int, y: float | None = None) -> float:
    return x * y if isinstance(y, float | int) else x * x 


def soma_2_num(x:int, y:int) -> int:
    return x + y if isinstance(y, int) else x + x 


soma_valores = mult(2, 2.2)
soma_valores2 = mult(2, 3)
# print(soma_valores)
# print(soma_valores2)


# Callable
#            Parâmetros da função   
#                         ↑          →  Retorno 
soma_ineiros = Callable[[int, int], int]

def executa(func: soma_ineiros, a:int, b:int) -> int:
    return func(a, b)


print(executa(soma_2_num, 5, 5))




# type vars
T = TypeVar('T')


def get_item(list: list[T], index: int) -> T:
    return list[index]


list_int = get_item([1,2,3], 1)
list_str = get_item(['a','b','c'], 1)


