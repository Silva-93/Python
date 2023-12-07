""" 
    As classes também possuem escopo (corpo) como as funções. O escopo é onde ficam os métodos da classe
"""


class Animal():
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'  # variável do escopo do init


    def comendo(self, alimento):
        return f'{self.nome} está comendo um(a) {alimento }'
    

    # Método que executa outro método
    def executa(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal('Leão')
print(leao.comendo('Zebra'))
print(leao.executa('Gnu'))
















