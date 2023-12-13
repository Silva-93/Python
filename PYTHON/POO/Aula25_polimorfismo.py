""" 
    Polimorfismo em python POO

    Polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse tenham métodos iguas (com a mesma assinatura) mas comportamentos diferentes.
    Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura).

    Opinião + pricípios que contam:
        Assinatura do método: nome, parâmetros e retorno iguais
    
    SO"L"ID (
        S = Single responsibility principle
        O = Open Close Principle 
        L = Liskov substitution principle
        I = Interface segregation principle
        D = Dependece inversion principle
    )

    Pincípio da substituição de liskov -> Objetos da uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação

    Sobrecarga de métodos (overload) -> python não suporta
    Sobreposição de métodos (override) -> python suporta
"""
from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg


    @abstractmethod
    def enviar(self) -> bool:
        ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.msg)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.msg)
        return True


# Polimorfismo
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada.')
    
    else:
        print('Notificação não enviada.')


notificacao_EMAIL = NotificacaoEmail('Testando e-mail')
notificar(notificacao_EMAIL)


notificacao_SMS = NotificacaoSMS('Testando SMS')
notificar(notificacao_SMS)