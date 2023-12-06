""" 
    __init__(): -> Inicializa os atributos da classe
    
    self -> Faz referência ao objeto que está sendo criado, ele é sempre o primeiro parâmetro do método. Ao chamar a classe, não necessário passar o self como parâmetro.

"""

class Pessoa:
    # atributos da classe ↓
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

#            nome      sobrenome
p1 = Pessoa('Jouber', 'Vicente')

print(p1.nome)
print(p1.sobrenome)


