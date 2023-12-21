import abc

# classe e métodos abstratos
class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self. conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...


    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO: {valor})')
        return self.saldo


    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é [{self.saldo:.2f}] {msg}')
        print('--' * 20)


    def __repr__(self) -> str:
        clas_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{clas_name} -> {attrs}'



# ContaPoupanca herda de Conta
class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE: {valor})')
            return self.saldo
        
        print('Não foi possível savar o valor desejado.')
        self.detalhes(f'(SAQUE NEGADO! Valor "{valor}" é insuficiente.)')
        return self.saldo



class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite


    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo =  -self.limite  # limite negativo, sempre vai ser um valor negativo

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUI: {valor}')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é: [{-self.limite:.2f}]')
        self.detalhes(f'(SAQUE de [{valor}] NEGADO!)')
        return self.saldo
    

    def __repr__(self) -> str:
        clas_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r}'
        return f'{clas_name} -> {attrs}'



if __name__ == '__main__':
    conta_poupanca_1 = ContaPoupanca(111, 222)
    conta_poupanca_1.sacar(1)
    conta_poupanca_1.depositar(2)
    print('###' * 30)
    conta_corrente = ContaCorrente(333, 444, 0, 100)
    conta_corrente.sacar(101)
    conta_corrente.depositar(32)
    






























