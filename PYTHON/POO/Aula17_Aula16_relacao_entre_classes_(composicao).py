""" 
    Relações entre classes: Composição

    Composição é uma especialização da agregação. Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.
"""


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []


    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))  # Criando a instâcia de endereço dentro da classe cliente (Composição)



    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero



cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua Tomé', 76)
cliente1.inserir_endereco('Rua França', 89)

cliente1.listar_enderecos()

# print(cliente1.enderecos[0].rua)  # Saida -> Av Brasil
# print(cliente1.enderecos[0].numero)  # Saida -> 54