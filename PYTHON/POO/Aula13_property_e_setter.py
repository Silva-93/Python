""" 
    Setter -> "Passa" por um método para configurar um atributo 

    getter - Pega um valor
    setter - Configura um valor

    Atributos que começam com "_" ou "__" (underlines) não devem ser usador fora da classe
"""


class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None


    # getter usado em python
    @property
    def cor(self):
        print('Usando a PROPERTY.')
        return self._cor
    


    @cor.setter
    def cor(self, valor):
        print('Passando pelo SETTER', valor)
        self._cor = valor


    @property
    def cor_tampa(self):
        return self._cor_tampa
    

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor



caneta = Caneta('Azul')
caneta.cor = 'Preta'
caneta.cor_tampa = 'Vermelha'

print(caneta.cor)
print(caneta.cor_tampa)