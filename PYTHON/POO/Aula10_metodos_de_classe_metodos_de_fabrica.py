""" 
    Métodos de classe e factories (fábricas)
    Métodos de classe -> São métodos onde "self" será "cls", ou seja, ao invés de receber a instâcia no primeiro parâmetro, receberá a prória classe. 

    factories -> Cria um novo objeto da classe
"""


class Pessoa:
    ano = 2023  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    # Método de classe
    @classmethod  
    def metodo_de_classe(cls):
        print('Hey')


    # método que cria um novo objeto
    @classmethod  
    def pessoa_mais_de_50_anos(cls, nome):
        return cls(nome, 50)


    @classmethod  
    def pessoa_sem_nome(cls, idade):
        return cls('Anônima', idade)



p1 = Pessoa('José', 32)
p2 = Pessoa.pessoa_mais_de_50_anos('Helena')
p3 = Pessoa.pessoa_sem_nome(20)

print(Pessoa.ano)
Pessoa.metodo_de_classe()

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
