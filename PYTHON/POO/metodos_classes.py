""" 
    Métodos de classe + factories (fábricas)

    São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro,
    recebemos a própria classe.
"""



class Person:
    age = 2023  # atributo de classe

    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Tranformando o método em um método da classe, podendo chamar esse método diretamente como se     fosse um atributo de classe.
    @classmethod  
    def method_class(cls):
        print('This is method')



    @classmethod  
    def create_with_50_age(cls, name):
        return cls(name, 50)



p1 = Person('João', 35)

p2 = Person.create_with_50_age('Marta')

print(p2.name, p2.age)

# Acessando o atributo da classe diretamente
print(Person.age)

# Chamando o método diretamente
Person.method_class()

