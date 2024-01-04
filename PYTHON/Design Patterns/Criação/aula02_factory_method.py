""" 
    Factory method é um padrão de criação que permite definir uma interface para criar objetos, mas deixa as subclasses decidirem queis objetos criar. O Factory method adia a instanciação para as subclasses, garantindo o baixo acoplamento entre classes.
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
        print('Carro popular está indo até o cliente.')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular está indo até o cliente.')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo está indo até o cliente.')


# Interface para criação de objetos
class VeiculoFactory(ABC):
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass # type: ignore


    def buscar_cliente(self):
        self.carro.buscar_cliente()


# Subclasse        Adicionando uma filial
class ZoneNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        if tipo == 'luxo':
            return CarroLuxo()
        
        if tipo == 'popular':
            return CarroPopular()
        
        if tipo == 'moto':
            return MotoLuxo()
        
        if tipo == 'moto de luxo':
            return MotoPopular()
        
        assert 0, 'Vaículo não existe'


# Subclasse
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe'


# Código cliente -> código que vai utilizar as classes
if __name__ == '__main__':
    from random import choice

    veiculos_disponiveis_ZN = ['luxo', 'popular', 'moto', 'moto de luxo']
    veiculos_disponiveis_ZS = ['popular']

    print('Zona Norte')
    for i in range(10):
        carro = ZoneNorteVeiculoFactory(choice(veiculos_disponiveis_ZN))
        carro.buscar_cliente()

    print()

    print('Zona Sul')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_ZS))
        carro2.buscar_cliente()