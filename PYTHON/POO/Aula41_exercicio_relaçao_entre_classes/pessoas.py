import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade


    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome



    @property
    def idade(self):
        return self._idade
    

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade


    def __repr__(self) -> str:
        clas_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{clas_name} -> {attrs}'



class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None




if __name__ == '__main__':
    cliente_1 = Cliente('Jouber', 30)
    cliente_1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(cliente_1)
    print(cliente_1.conta)

    cliente_2 = Cliente('Maria', 20)
    cliente_2.conta = contas.ContaPoupanca(333, 444, 100)
    print(cliente_2)
    print(cliente_2.conta)







