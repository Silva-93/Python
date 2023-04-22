"""
    O módulo OS é usado para interagir com o SO, por exemplo, o módulo os.path contém funções para trabalhar com caminhos de arquivos e a função os.listdir() pode ser usada para listar os arquivos em um diretório. O método os.system() permite executar comandos do SO a partir do seu código python.
"""
import os

os.system('cls')

""" 
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80) 
"""

"""
    os.path trabalha com caminhos em windows, linux e mac, é um módulo que fornece funções para trabalhar com caminhos de arquivos nos SOs sem precisar se preocupar com as diferenças entre os sistemas.
    
    Exemplo do os.path
    os.path.join('pasta1', 'pasta2', 'arquivo.txt')  -> Junta strings em um único caminho.
        saída -> 'pasta1\pasta2\arquivo.txt'

    os.path.split  -> Divide um caminho em uma tupla (diretório, arquivo).
        os.path.split('/home/user/arquivo.txt)
            saída -> ('/home/user', 'arquivo.txt')
    
    os.path.exists  -> Verifica se um caminho especificado existe

    O os.path só trabalha com caminhos de arquivos e não faz nenhuma operação de netrada/saída com arquivos em si.
"""

caminho = os.path.join('C:\Users\Jouber')