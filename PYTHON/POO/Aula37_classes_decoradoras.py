""" 
    Classes decoradoras (Decorator Classes)
"""

class Multiplicar:
    def __init__(self, func) -> None:
        self.func = func
        self._multiplicador = 10


    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result * self._multiplicador


@Multiplicar
def soma(x: int, y: int):
    return x + y


soma_2_2 = soma(2, 2)

print(soma_2_2)