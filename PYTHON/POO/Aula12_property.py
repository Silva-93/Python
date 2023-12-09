""" 
    @property -> Um getter no modo pythônico. 
    getter - é um método para obter um valor de um determinado atributo

    @property -> É uma propriedade do objeto, ela é um método que se comporta como um atributo. Geralmente é usada nas seguintes situações:
        como getter
        p/ evitar quebrar código cliente
        p/ habilitar o setter
        p/ executar ações ao obter um atributo
"""

class Caneta:
    def __init__(self, cor):
        self.cor = cor




caneta = Caneta('Azul')
print(caneta.cor)