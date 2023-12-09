""" 
    Encapsulamento (modificadores de acesso: public, protected e private)

    Python não tem modificadores de acesso, mas pode ser seguido as seguintes convenções

      (sem underline) = public -> Pode ser usado em qualquer lugar

    _ (um underline) = protected -> Não deve ser usado fora da classe ou subclasses.
    
    __ (dois underline) = pivate -> "name mangling" (desfiguração de nomes) em python só deve ser usado na classe em que foi declarado.
"""

class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'


    def metodo_publico(self):
        return 'Metodo público'


    def _metodo_protected(self):
        self.__metodo_privado()
        return '_metodo protegido'


    def __metodo_privado(self):
        print('Isso é privado')
        return 'Isso é privado'  


f = Foo()
print(f.public)
print(f.metodo_publico())

print(f._protected)  # isso não deve ser executado dessa forma
print(f._metodo_protected())  # isso não deve ser executado dessa forma

