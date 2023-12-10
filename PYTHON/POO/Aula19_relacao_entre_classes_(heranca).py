""" 
    Associação -> Usa outro objeto
    Agregação -> Tem outro objeto
    Composição -> É dono de outro objeto
    Herança -> Uma classe extende outra classe, tudo que há um uma super classe será herdada para classe filha.

    Quando uma classe é criada e outras classes vão herdá-la, ele é chamada de dessas formas "super class, base class e parent class"

    As classes filhas são classes que herdam atributos de outra classe, podem ser chamadas de "sub class, child class e derived class"


    No python, todas as classes herdam automaticamente de um builting object, esse object cria um objeto vazio

"""

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)  # sabendo o nome da classe



class Cliente(Pessoa):  # Criando a herença entre cliente e pessoa, todos os atributos de Pessoa (classe pai) vão ser herdados para a classe Cliente (classe filha)
    ...



class Aluno(Pessoa):
    ...


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()

a1 = Aluno('Maria', 'Luiza')
a1.falar_nome_classe()
































