""" 
    Exercício com classes

    1- Crie uma classe Carro (nome) 
    2- Crie uma classe Motor (nome) 
    3- Crie uma classe Fabricante (nome) 
    4- Faça a ligação entre Carro tem um Motor (Obs.: Um motor pode ser de vários carros)
    5- Faça a ligação entre Carro e um Fabricante (Obs.: Um fabricante pode ter vários carros)

    Exiba o nome do carro, motor e fabricantes na tela
"""



class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor


    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor




class Motor:
    def __init__(self, nome):
        self.nome = nome



class Fabricante:
    def __init__(self, nome):
        self.nome = nome


# Associando o carro a um fabricante
fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
fusca.fabricante = volkswagen

# Associando um carro a um moto
motor_1_0 = Motor('1.0')
fusca.motor = motor_1_0

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)