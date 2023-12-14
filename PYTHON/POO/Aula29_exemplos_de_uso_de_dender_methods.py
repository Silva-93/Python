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
    def __init__(self, x, y):
        self.x = x
        self.y = y


    # representação -> Mais utilizado para comunicar a outros desenvolvedores como quer que o objeto seja criado
    def __repr__(self) -> str:
        class_name = type(self).__name__  # sabendo o nome da classe
        return f'{class_name}(x={self.x!r}, y={self.y!r})'



    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    

    # verificando se o self é maior que o other
    def __gt__(self, other):
        resultado_self = self.x + self.x
        resultado_other = other.x + other.y
        return resultado_self > resultado_other
    



if __name__ == '__main__':

    p1 = Ponto(2, 3)  # 5
    p2 = Ponto(12, 21)  # 33
    p3 = p1 + p2

    print(p3)

    print('P1 é maior que p2', p1 > p2)  # False
    print('P2 é maior que p2', p2 > p1)  # True