# Herança simples - Relações entre classes

# Associação - usa um objeto 

# Agregação - tem um objeto

# Composição - É dono de objeto

# Herança - É um objeto

# Herança vs Composição

# Classe principal (Pessoa)
#   -> super class, base class, parent class

# Classes filhas (Cliente)
#   -> sub class, child class, derived class



# Herança simples

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)  # identifica a classe que pertence.


class Cliente(Pessoa):  # Herdando a classe cliente
    ...


class Aluno(Pessoa):
    ...

c1 = Cliente('Jouber', 'Vicente')
print(c1.nome, c1.sobrenome)  # A classe clente herdou as instâncias da classe Pesso
c1.falar_nome_classe()

a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()

