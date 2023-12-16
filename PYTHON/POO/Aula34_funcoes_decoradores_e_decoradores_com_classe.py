""" 
    Funções decoradoras e decoradores com classes
"""

# criando uma função quer vai servir como um __repr__
def my_repr(self) -> str:
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name} ({class_dict})'
    return class_repr



# função decoradora
def add_repr(cls):
    cls.__repr__ = my_repr
    return cls



@add_repr  # decorador
class Time():
    def __init__(self, name) -> None:
        self.name = name


@add_repr
class Planet:
    def __init__(self, name) -> None:
        self.name = name



brasil = Time('Brasil')
portugal = Time('Portugal')


terra = Planet('Terra')
marte = Planet('Marte')


print(brasil)

print(terra)














