# class - Classes são moldes para criar novos objetos As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.

# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.

# Por convenção, usamos PascalCase para nomes de classes.

# string = 'Luiz'  # str

# print(string.upper())

# print(isinstance(string, str))


# Criando uma classe com dois atributos
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Jouber', 'Vicente')

""" 
print(p1.nome)
print(p1.sobrenome)
"""

# Métodos em instâcias de classes Python

class Carro:
    def __init__(self, nome):
        self.nome = nome

    # Métodos da classe
    def acelerar(self):
        print(f'{self.nome} está acelerando')


celta = Carro('Celta')
celta.acelerar()  # chamando a classe com o método.