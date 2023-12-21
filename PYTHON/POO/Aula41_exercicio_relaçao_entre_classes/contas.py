import abc

# classe e métodos abstratos
class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self. conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor): ...


    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO: {valor})')


    def detalhes(self, msg=''):
        print(f'O seu saldo é [{self.saldo:.2f}] {msg}')
        print('--' * 20)



# ContaPoupanca herda de Conta
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE: {valor})')
            return self.saldo
        
        print('Não foi possível savar o valor desejado.')
        self.detalhes(f'(SAQUE NEGADO! Valor "{valor}" é insuficiente.)')



if __name__ == '__main__':
    conta_poupanca_1 = ContaPoupanca(111, 222, 10)
    conta_poupanca_1.sacar(1)

    conta_poupanca_1.depositar(2)






























