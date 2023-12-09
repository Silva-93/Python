""" 
    Relações entre classes: associação.

    Associação é um tipo de relação onde os objetos estão ligados dentro do sistema. Essa é relação mais comum entre objetos e tem subconjuntos como agregação e composição. Geralmente, temos um associação quando um objeto tem um atributo que referencia outro objeto. A associação não especifica como um objeto controla o ciclo de vida de outro objeto. 
"""

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.maquina = None


    @property
    def maquina(self):
        return self._maquina
    

    @maquina.setter
    def maquina(self, maquina):
        self._maquina = maquina



class MaquinaDeEscrever:
    def __init__(self, nome):
        self.nome = nome


    def escrever(self):
        return f'{self.nome} está escrevendo.'
    


escritor = Escritor('Luiz')
datilografia = MaquinaDeEscrever('Maquina datilografia')
escritor.maquina = datilografia  # associando a classe "Escritor" com a classe "MaquinaDeEscrever"

print(datilografia.escrever())  # saida -> Maquina datilografia está escrevendo.
print(escritor.maquina.escrever())  # saida -> Maquina datilografia está escrevendo.