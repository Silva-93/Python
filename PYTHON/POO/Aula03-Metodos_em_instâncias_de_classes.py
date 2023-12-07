""" 
    Instância e objetos normalmente se referem a mesma coisa.

    Todo método recebe como primeiro argumento o "self"        
"""

class Carro:
    def __init__(self, marca, modelo, ):
        self.marca = marca
        self.modelo = modelo

    # Métodos
    def acelerar(self):
        return f'O {self.modelo} está acelerando...'


fusca = Carro('Volkswagen', 'Fusca')

print(fusca.marca, fusca.modelo)
print(fusca.acelerar())  # chamando a classe com o método


















