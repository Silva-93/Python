

class Multiplicacao:
    """ Documentação da classe """

    def multiplicar(self, x: int | float, y: int | float, z: int | float | None = None) -> int | float:
        """ Multiplica x, y e/ou z

            Multiplica x e y. Se z for enviado, multiplica x, y e z
        """

        if z is None:
            return x * y
        
        return(x * y * z)