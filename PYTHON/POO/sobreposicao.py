"""
    super() -> É a super classse na sub classe

    Classe pricipal (Pessoa)
        -> super class, base class, parent class

    Classes filas (Cliente)
        -> sub class, child class, derived class
"""


class MinhaString(str):
    def upper(self):
        print('Antes do upper()')
        retorno = super(MinhaString, self).upper()  # Retorna temporariamente a super classe
        print('Depois do upper()')
        return retorno

string = MinhaString('Jouber')
print(string.upper())