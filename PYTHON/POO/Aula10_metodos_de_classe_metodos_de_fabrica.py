""" 
    Métodos de classe e factories (fábricas)
    Métodos de classe -> São métodos onde "self" será "cls", ou seja, ao invés de receber a instâcia no primeiro parâmetro, receberá a prória classe. 
"""


class Pessoa:
    ano = 2023  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    # Método de classe
    @classmethod
    def metodo_de_clase