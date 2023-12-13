""" 
    Criando exceptions em POO

    Para criar uma exception em python, você só  porecisa herdar de alguma exceção da linguagem. A recomendação da doc é herdar de exception.

    Criando exceções (comum colocar error ao final)
    Levantando (raise)
    Lançando (throw) exceções
    Relançando exceções
"""




class MeuError(Exception):
    ...



class OutroError(Exception):
    ...




def levantar():
    exception_ = MeuError('A', 'B', 'C')
    
    raise exception_


# tratando a exceção
try:
    levantar()

except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = OutroError('Outro error')

    raise exception_ from error