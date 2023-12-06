""" 
    1° -> Recebe um número inteiro
    2° -> Saber se o número é multiplo de 3 e 5
        Bacon com Ovos
    
    3° -> Saber se o número é somente multiplo de 3
    4° -> Saber se o número é somente multiplo de 5
    5° -> Server se o número não é multiplo de 3 e 5
        Passar fome!
"""


def bacon_com_ovos(n):
    assert isinstance(n, int), '"n" deve ser um número int.'

    if n % 15 == 0:
        return 'Bacon com Ovos'
    
    if n % 3 == 0:
        return 'Bacon'

    if n % 5 == 0:
        return 'Ovos'

    return 'Passar fome!'









