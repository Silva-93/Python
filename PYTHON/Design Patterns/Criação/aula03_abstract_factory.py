""" 
    Abstract Factory é um padrão de criação que fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. Geralmente Abstract Factory conrta com um ou mais Factory Mathods para criar seus objetos.

    Uma diferença importante entre Factory method e abstract factory é que o factory method usa herenaça, enquanto abstract factory usa a composição.

    Princípio: programe para interfaces, não para im plementações.
"""

from abc import ABC, abstractmethod

# Interface
class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass

# Interface
class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


# ZONA NORTE
class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN está indo até o cliente.')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZN está indo até o cliente.')


class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZN está indo até o cliente.')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS está indo até o cliente.')


# ZONA SUL
class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS está indo até o cliente.')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZS está indo até o cliente.')


class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZS está indo até o cliente.')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS está indo até o cliente.')


# Interface para criação de objetos
class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular: pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo(tipo: str) -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular: pass


################ Adicionando uma filial ################


# Subclasse
class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()


# Subclasse
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()

# (Composição)
class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()


# Código cliente -> código que vai utilizar as classes
if __name__ == '__main__':
    cliente = Cliente()
    cliente.busca_clientes()
