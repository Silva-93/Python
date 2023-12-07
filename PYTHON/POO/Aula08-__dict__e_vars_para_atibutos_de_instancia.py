""" 
    __dict__ e vars -> Mantem um objeto do tipo "dicionário" (maping) dentro do objeto que mantem os valorem que podem ser escritos dentro objeto


"""

class Pessoa:
    ano_atual = 2023  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

# p1 = Pessoa('Jouber', 30)
# print(p1.__dict__)  # saida -> {'nome': 'Jouber', 'idade': 30}
# print(vars(p1))  # saida -> {'nome': 'Jouber', 'idade': 30}  |  chama o __dict__

# Desempacotando o dicionário
dados = {'nome': 'Jouber', 'idade': 30}
p1 = Pessoa(**dados)

print(vars(p1))  # saida -> {'nome': 'Jouber', 'idade': 30}