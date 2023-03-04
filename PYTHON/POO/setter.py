# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None


    @property # getter -> Obtem o valor
    def cor(self):
        print('Property')
        return self._cor
    

    @cor.setter  # Configura o valor
    def cor(self, valor):
        print('Aqui é o SETTER, ', valor)
        self._cor = valor


    @property
    def cor_tampa(self):
        return self._cor_tampa
    

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor



caneta = Caneta('Azul')
caneta.cor = 'Verde'
print(caneta.cor)