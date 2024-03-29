""" 
   Bridge é um padrão de projeto estrutural que tem a intenção de desacoplar um abstração de sua implementação, de modo que as duas possam variar e evoluir independetemente.

   Abstração é uma camada de alto nível para algo. Geralmente, a abstração não faz nenhum trabalho por contra própria, ela delega parte ou todo o trabalho para a camada de implementação.

   RELEMBRANDO: Adapter é um pedrão de projeto estrutural que tem a intenção depermitir que duas classes que seriam incomplatíveis trabalhem em conjunto através de um "adaptador".

   Diferença (GoF pag. 208) - A diferença chave entre esses padrões está nas suas intenções... O padrão adapter faz as coisas funcionarem APÓS elas terem sido projetadas; o Bridge as fa funcionar ANTES QUE exitam... 
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: pass


    @abstractmethod
    def decrease_volume(self) -> None: pass


    @abstractmethod
    def power(self) -> None: pass



class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device


    def increase_volume(self) -> None: 
        self._device.volume += 10


    def decrease_volume(self) -> None: 
        self._device.volume -= 10


    def power(self) -> None: 
        self._device.power = not self._device.power


class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    def volume(self, volume: int) -> None: pass


    @property
    @abstractmethod
    def power(self) -> int: pass

    @power.setter
    def power(self, power: bool) -> None: pass


class TV(IDevice):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int: 
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None: 
        if not self.power:
            print(f'Please, turn {self._name} ON')
            return

        if volume < 0: 
            return
        
        if volume > 100:
            return

        self._volume = volume
        print(f'Volume is now: {self._volume}')

    @property
    def power(self) -> int: 
        return self._power

    @power.setter
    def power(self, power: bool) -> None: 
        self._power = power
        power_status = 'ON' if self._power else 'OFF'

        print(f'{self._name} is now {power_status}')



if __name__ == '__main__':
    tv = TV()
    remote = RemoteControl(tv)

    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    
    remote.power()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    
    remote.power()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()





