import contas
import pessoas


class Banco:
    def __init__(
        self, 
        agencias: list[int] | None = None, 
        clientes: list[pessoas.Pessoa] | None = None, 
        contas: list[contas.Conta] | None = None
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []



    def _checa_agencia(self, agencia):
        if agencia.agencia in self.agencias:
            return True
        return False



    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False



    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False
    


    def _checa_conta_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False



    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
                self._checa_cliente(cliente) and \
                self._checa_conta(conta) and \
                self._checa_conta_cliente(cliente, conta)
    

    def __repr__(self) -> str:
        clas_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{clas_name} -> {attrs}'



if __name__ == '__main__':
    cliente_1 = pessoas.Cliente('Jouber', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    cliente_1.conta = cc1

    cliente_2 = pessoas.Cliente('Maria', 20)
    cp1 = contas.ContaPoupanca(333, 444, 100)
    cliente_2.conta = cp1 

    banco = Banco()
    banco.agencias.extend([111, 333])
    banco.clientes.extend([cliente_1, cliente_2])
    banco.contas.extend([cc1, cp1])
    
    
    
    if banco.autenticar(cliente_1, cc1):
        cc1.depositar(10)
        print(cliente_1.conta)
















