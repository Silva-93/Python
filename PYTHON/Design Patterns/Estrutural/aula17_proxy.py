""" 
    O proxy é um padrão de projeto estrutural que tem a intenção de fornecer um objeto substitiuto que atua como se fosse o objeto real que o código cliente gostaria de usar. O proxy receberá as solicitações e terá controle sobre como e quando repassar tais solicitações ao objeto real.

    Com base no modo como o proxies são usados, nós os classificamos como:
        
        Proxy virtual: Controla acesso a recursos que podem ser caros para criação ou utilização.
        Porxy Remoto: Controla acesso a recursos que estão em servidores remotos.
        proxy de proteção: controla acesso a recursos que possam necessitar autenticação ou permissão.
        Proxy inteligente: Além de controlar acesso ao objeto real, também executa tarefas adicionais para saber quadno e como executar determinadas ações.

    Proxys podem fazer várias coisas diferentes:
        crias logs, autenticar usuários, destribuir serviços, cirar cache, criar e destrir objetos, adiar execuções e muito mais...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep


# Subject Interface
class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> list[dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> dict: pass

# Real subject
class RealUser(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # Simulando requisição
        self.firstname = firstname
        self.lastname = lastname
    
    def get_addresses(self) -> list[dict]: 
        sleep(2)  # Silumando requisição
        return [
            {'rua': 'Av. Brasil', 'numero': 500},
        ]

    def get_all_user_data(self) -> dict: 
        sleep(2)
        return {
            'cpf': '111.111.111-11',
            'rg': '8.122.344'
        }

# Proxy
class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser
        self._cached_addresses: list[dict]
        self._all_user_data: dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)


    def get_addresses(self) -> list[dict]: 
        self.get_real_user()
        
        if not hasattr(self, '_chached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()
        
        return self._cached_addresses


    def get_all_user_data(self) -> dict: 
        self.get_real_user()
        
        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        
        return self._all_user_data



if __name__ == '__main__':
    luiz = UserProxy('Luiz', 'Otávio')

    print(luiz.firstname)
    print(luiz.lastname)

    print(luiz.get_all_user_data())
    print(luiz.get_addresses())

    # responde instantaneamente
    for i in range(50):
        print(luiz.get_addresses())