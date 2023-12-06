# class - Classes são moldes para criar novos objetos As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.

# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.

# Por convenção, usamos PascalCase para nomes de classes.

# string = 'Luiz'  # str

# print(string.upper())|

# print(isinstance(string, str))


# Criando uma classe com dois atributos
class Pessoa:
    # atributos da classe ↓
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Jouber', 'Vicente')


print(p1.nome)
print(p1.sobrenome)


