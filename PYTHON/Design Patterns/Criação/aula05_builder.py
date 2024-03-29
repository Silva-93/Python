""" 
    Builder é um padrão de criação que tem a intenção de separar a construção de um objeto complexo da sua representação, de modo que o mesmo processo de construnção possa criar diferentes representações.

    Builder te da a possibilidade de criar objetos passo-a-passo e isso já é possível no Python sem este padrão.

    Geralmente o builder aceita o encadeamento de métodos (method chaining)
"""
from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'  # retorna o nome da classe e o que ela recebe


    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin): 
    def __init__(self) -> None:
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone = []
        self.address = []


# Interface
class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstname(self, firstname): pass

    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_address(self, address): pass


class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname): 
        self._result.firstname = firstname

    def add_lastname(self, lastname): 
        self._result.lastname = lastname

    def add_age(self, age): 
        self._result.age = age

    def add_phone(self, phone): 
        self._result.phone.append(phone)

    def add_address(self, address): 
        self._result.address.append(address)


class UserDirector: 
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder


    def with_age(self, firstname, lastname, age):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        return self._builder.result


    def with_address(self, firstname, lastname, address):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_address(address)
        return self._builder.result




if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Jouber', 'Vicente', 30)
    user2 = user_director.with_address('Ketilin', 'Brenda', 'Av Sebastião Salazar')

    print(user1)
    print(user2)
