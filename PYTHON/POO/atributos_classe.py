# Atributos de classe -> Este atributo tem o mesmo valor em todas os métodos da classe

class Pessoa:
    # ↓ Atibuto da classe
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    


p1 = Pessoa('Joao', 30)

p2 = Pessoa('Marta', 25)

""" print(p1.ano_nascimento())
print(p2.ano_nascimento()) """

# __dict__ -> Local onde ficam armazenados os valores das instâncias da classe. Retorna um dicionário
# Os valores contidos no __dict__ podem ser alterados. (Não muito usado)

print(p1.__dict__)

print(vars(p1))  # Mesmo que o __dict__