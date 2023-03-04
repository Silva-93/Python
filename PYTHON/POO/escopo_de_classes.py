# Escopo de classe e de métodos da classe

class Animal:
    # Escopo da classe ↓

    def __init__(self, nome):
        
        # Atributos de instância 
        self.nome = nome

    # Métodos da classe ↓ 

    def acao(self):
        return f'{self.nome} está executando uma ação'


    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'


    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal('Leão')

print(leao.acao())

print(leao.comendo('Zebra'))

print(leao.executar('Gnu'))







