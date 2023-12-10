""" 
    super() -> é a super classe na sub classe, o super() retorna temporáriamente a super classe e torna possível chamar métodos da super classe.
"""

class MinhaString(str):
    def upper(self):
        print('chamou UPPER')
        retorno =  super().upper()  # sobreponto um método, supoer() está retornando a classe "str"
        print('depois do UPPER')
        return retorno


# string = MinhaString('Jouber')
# print(string.upper())




class A:
    atributo_a = 'Valor A'

    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'Valor B'
    
    def __init__(self, atributo, valor_qualquer):
        super().__init__(atributo)
        self.valor_qualqer = valor_qualquer

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'Valor C'
    
    def __init__(self, *args, **kwargs):
        print('Executei primeiro')
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo()  # saida -> B
        super(B, self).metodo()  # saida -> A  |  a partir de "B" procura a função  "metodo()" para executá-la
        print('C')


c = C('atributo', 'Valor qualquer')
print(c.atributo)   
print(c.valor_qualqer)   

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)

# c.metodo()



