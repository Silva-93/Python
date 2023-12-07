""" 
    Atributo de classe são "variáveis" que estão no escopo da classe, podem ser usadas fora da classe
"""

class Pessoa:
    ano_atual = 2023  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Jouber', 30)


print(Pessoa.ano_atual)  # Chamando o atributo da classe fora da classe
print(p1.ano_nascimento())