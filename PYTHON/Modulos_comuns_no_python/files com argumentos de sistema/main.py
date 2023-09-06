""" 
    sys.argv -> Executando arquivos com argumentos de sistema

    O 1° argumento é sempre o script que está sendo executado

"""

import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos.')
else:
    print(f'Você passou {qtd_argumentos} de argumentos e foram {argumentos[1:]}')