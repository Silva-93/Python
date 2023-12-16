""" 
    Context Manger com função - Criando e usando gerenciadores de context
"""

from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    try:
        print('Abrindo o arquivo')
        file = open(path, mode, encoding='utf8')
        yield  file  # faz com que a função se torne uma função geradora
        
    except Exception as e:
        print('Ocorreu o erro: ', e)

    finally:
        print('Fechando o arquivo')
        file.close()


with my_open('Aula33_contextlib_contextmanager.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    print('WITH', file)