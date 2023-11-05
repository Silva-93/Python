""" 
    Crie um programa que tenha um função fatorial() que receba dois parâmetro o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de calcular o fatorial. 
"""

def fatorial(n, show=False):
    """ 
    -> Calcular o fatorial de um número.
    :parâmetro n: O número a ser calculado.
    :parâmetro show: (opcional) Mostra ou não a conta.
    :return: O valor fatorial de um número n.
    """
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
    return f

help(fatorial)
print(fatorial(10, show=True))






