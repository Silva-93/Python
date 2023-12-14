# python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str



class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z


    # representação de string - como a string será exibida
    def __str__(self) -> str:
        return f'{self.x}, {self.y}'


    # representação -> Mais utilizado para comunicar a outros desenvolvedores como quer que o objeto seja criado
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}), z={self.z!r}'


p1 = Ponto(1, 2)
p2 = Ponto(1423, 7899)

print(p1)

# vendo o repr
print(repr(p2))
# ou  | s = string | r = repr
print(f'{p2!r}')









