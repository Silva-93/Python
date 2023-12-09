""" 
    @property -> Um getter no modo pythônico. 
    getter - é um método para obter um valor de um determinado atributo

    @property -> É uma propriedade do objeto, ele faz um método se comportar como um atributo, com isso não é necessário usar os "()" para chamar o método. Geralmente é usada nas seguintes situações:
        como getter
        p/ evitar quebrar código cliente
        p/ habilitar o setter
        p/ executar ações ao obter um atributo
"""

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor



    # getter normalmente usado em outras linguagens de programação
    # def get_cor(self):
    #     return self.cor


    # getter usado em python
    @property
    def cor(self):
        print('Usando a PROPERTY.')
        return self.cor_tinta


    @property
    def cor_tampa(self):
        return 'Tampa azul'



caneta = Caneta('Azul')
# print(caneta.get_cor())
print(caneta.cor)
print(caneta.cor_tampa)