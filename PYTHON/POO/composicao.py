# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []


    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))


    def listar_endereco(self):
        print()
        for endereco in self.enderecos:
            print(endereco.rua, '-',endereco.numero)




class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


    def __del__(self):
        print('Apagando', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 23)
cliente1.listar_endereco()

del cliente1

print('######## Aqui acaba o código ########')
