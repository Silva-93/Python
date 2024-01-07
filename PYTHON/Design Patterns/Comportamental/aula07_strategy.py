""" 
    Strategy é um padrão de projeto comportamental que tem a intenção de definir um família de algoritmos, encapsular cada uma delas e torná-las intercambiáveis. Strategy permite que o algorítmo varie independentemente dos clientes que o utilizam.

    Princípio:
    Entidades devem ser abertas para extensão, mas fechadas para modificação.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

# contexto (Pedido)
class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount


    @property
    def total(self):
        return self._total
    

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


# strategy
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass
        

class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount) -> None:
        self.discount = discount / 100
    
    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == '__main__':
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    five_percent = CustomDiscount(5)

    order = Order(1000, twenty_percent)
    print(f'Preço total: {order.total} \nPreço com 20% de desconto: {order.total_with_discount}')

    order = Order(1000, fifty_percent)
    print(f'Preço total: {order.total} \nPreço com 20% de desconto: {order.total_with_discount}')

    order = Order(1000, no_discount)
    print(f'Preço total: {order.total} \nPreço sem de desconto: {order.total_with_discount}')

    order = Order(1000, five_percent)
    print(f'Preço total: {order.total} \nPreço com 5% de desconto: {order.total_with_discount}')


















