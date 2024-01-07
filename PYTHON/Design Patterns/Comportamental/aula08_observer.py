""" 
    O padrão observer tem a intenção de definir uma dependência de um-para-muitos entre objetos, de maneira que quando um objeto muda de estado, todo os seus dependentes são notificados e atualizados automaticamente. 

    Um observer é um objeto que gostaria de ser informado, um observable(subject) é a entidade que gera as informações.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

# Interface
""" Observable """
class IObservable(ABC): 
    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remover_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass

    @property
    @abstractmethod
    def state(self) -> None: pass



class WeatherStation(IObservable):
    def __init__(self):
        self._observers: list[IObserver] = []
        self._state: dict = {}

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state_update: dict) -> None:
        new_state: dict = {**self._state, **state_update}
        
        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()


    def add_observer(self, observer: IObserver) -> None: 
        self._observers.append(observer)

    def remover_observer(self, observer: IObserver) -> None: 
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notify_observers(self) -> None: 
        for observer in self._observers:
            observer.update()
        print()


""" Observer """
class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name}: o objeto "{observable_name}" acabou de ser atualizado -> {self.observable.state}')




if __name__ == '__main__':
    weather_station = WeatherStation()

    smartphone = Smartphone('IOS', weather_station)
    outro_smartphone = Smartphone('Android', weather_station)
    
    weather_station.add_observer(smartphone)
    weather_station.add_observer(outro_smartphone)

    weather_station.state = {'temperature': '30'}
    weather_station.state = {'temperature': '35'}
    weather_station.state = {'temperature': '30', 'humidity': '90'}

    weather_station.remover_observer(outro_smartphone)
    weather_station.reset_state()
