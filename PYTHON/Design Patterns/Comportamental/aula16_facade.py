""" 
    Façade (Fachada) é um padrão de projeto estrutural que tem a intenção de fornecer uma interface unificada para um conjunto de interfaces um um subsistema. Façade define uma interface de nível mais alto que torna o subsistema mais fácil de ser usado. 
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




class WeatherStationFacade:
    def __init__(self) -> None:
        
        self.weather_station = WeatherStation()

        self.smartphone = Smartphone('IOS', self.weather_station)
        self.outro_smartphone = Smartphone('Android', self.weather_station)
        
        self.weather_station.add_observer(self.smartphone)
        self.weather_station.add_observer(self.outro_smartphone)


    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)


    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.remover_observer(observer)

    
    def change_state(self, state: dict) -> None:
        self.weather_station.state = state


    def remove_smartphone(self) -> None:
        self.weather_station.remover_observer(self.smartphone)


    def reset_state(self) -> None:
        self.weather_station.reset_state()


if __name__ == '__main__':
    weather_station = WeatherStationFacade()

    weather_station.change_state({'temperature': '30'}) 
    
    weather_station.remove_smartphone()
    weather_station.reset_state()

    weather_station.change_state({'temperature': '35'}) 
    weather_station.change_state({'temperature': '30', 'humidity': '90'}) 































