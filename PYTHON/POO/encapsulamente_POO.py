# Encapsulamento (modificadores de acesso: public, protected, private)

# Python NÃO TEM modificadores de acesso mas podemos seguir as seguintes convenções

#   (sem underline) = public
#       pode ser usado em qualquer lugar

# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.

# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'Público'
        self._protected = 'Protegido'
        self.__private = 'Privado'

    def metodo_publico(self):
        return 'Metodo publico'
    

    def _metodo_protected(self):
        return '_Metodo_protegido'


    def __metodo_privado(self):
        return '__Metodo_privado'



f = Foo()
print(f.public)
print(f.metodo_publico())

