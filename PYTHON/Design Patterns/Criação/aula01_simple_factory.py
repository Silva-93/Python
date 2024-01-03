""" 
    Naprogramação POO, o termo factory (fábrica) refere-se a uma classe ou método que é responsável por criar objetos.

    Vantagens:
        Permitem criar um sistema com baixo acoplamento entre classes porque ocultam as classes que criam os objetos do código cliente.

        Facilitam a adição de novas classes ao código, porque o cliente não conhece e nem utiliza a implementação da classe (utiliza a factory).

        Podem facilitar o processo de "cache" ou criação de "singletons" porque a fábrica pode retornar um objeto já criado para o cliente, ao invés de criar novos objetos sempre que o cliente precisar.

    Desvantagens:
        Podem introduzir muitas classes no código

    Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

    Nessa aula:
    Simple Factory: Uma espécie de factory method parametrizado
    Simple Factory: Pode não ser considerado um padrão de projeto por si só
    Simple Factory: Pode quebrar pricípios do SOLID
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está indo até o cliente.')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de popular está indo até o cliente.')


# simple factory
class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        if tipo == 'luxo':
            return CarroLuxo()
        
        if tipo == 'popular':
            return CarroPopular()
        
        assert 0, 'Vaículo não existe'


if __name__ == '__main__':
    from random import choice

    carros_disponiveis = ['luxo', 'popular']

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()