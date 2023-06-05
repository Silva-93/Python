"""
    O módulo OS é usado para interagir com o SO, por exemplo, o módulo os.path contém funções para trabalhar com caminhos de arquivos e a função os.listdir() pode ser usada para listar os arquivos em um diretório. O método os.system() permite executar comandos do SO a partir do seu código python.
"""
import os
import shutil

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

""" caminho = os.path.join('Desktop', 'curso', 'arquivo')
print(caminho)

diretorio, arquivo = os.path.split(caminho)  # Dividindo o caminho do arquivo
print(arquivo), print(diretorio)

print(os.path.exists(caminho))  # Verificando se o caminho exite, retorna True ou False

print(os.path.abspath('.'))  # Retorna o caminho absoluto de um arquivo ou diretório

print(os.path.basename(caminho))  # Retorna o final do caminho
 """


"""
    os.listdir  -> Usado para listar diretórios
"""

""" caminho = os.path.join('C:\\', 'Users', 'Jouber', 'Desktop')

for pasta in os.listdir(caminho):   
    path_full = os.path.join(caminho, pasta)  # listando o camiho completo mais as pastas 
    print(pasta)  # Mostrando as pastas
    
    if not os.path.isdir(path_full):  #  Verificando se não é um diretório
        continue
    
    for itens in os.listdir(path_full):  # Listando o conteúdo dentro das pastas
        print('     ', itens) """


"""
    os.walk  -> É uma função que permite percorrer uma estrutura de diretórios de maneira recusiva. Ela gera uma sequência de tuplas, onde cada tupla possui três elementes: o diretório atual(root), uma lista de subdiretórios(dirs) e uma lista dos arquivos do diretório atual(files).
"""

""" caminho = os.path.join('C:\\', 'Users', 'Jouber', 'Desktop')

for root, dirs, files in os.walk(caminho):
    print('Pasta atual', root)  # Listando os diretórios "principais"

    for dir_ in dirs:  #  Listando os subdiretórios
        print('    ', 'Dir: ', dir_)

    for file_ in files:  # Listando os arquivos dentro de todos os diretórios
        print('        ', 'Files: ', file_) """


""" 
    os.path.getsize e os.stat para dados dos arquivos
"""

# Convertendo o tamanho do arquivo de bytes para outras grandesas

""" import math

def format_size(size_bytes: int, base: int = 1000) -> str:
    #Formata um tamanho de bytes para o  tamanho apropriado

    if size_bytes <= 0:
        return '0B'

    # Tupla com os tamanhos
    abreviattion_size = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'

    # math.log vai retornar o algoritmo do size_bytes
    index_abreviattion_siza = int(math.log(size_bytes, base))

    # Por quanto o tamanho deve ser dividido para gerar o tamanho correto
    power = base ** index_abreviattion_siza

    # Tamanho final
    final_size = round(size_bytes/power, 2)

    # Abreviação do tamanho
    abreviattion_size = abreviattion_size[index_abreviattion_siza]

    return f'{final_size} {abreviattion_size}'

print(format_size(1000))
print(format_size(1000000))
print(format_size(1000000000))
print(format_size(1000000000000))
print(format_size(1000000000000000)) """


# Copiando arquivos, movendo arquivos, renomeando arquivos, criando/apagando diretórios...

""" 
    Mover/Renomear -> shutil.move()
    Mover/Renomear -> os.rename()

    Copiar -> shutil.copy() / shutil.copytree()

    Apagar -> os.unlink()

    Apagar diretório recursivamente -> shutil.rmtree()
"""

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
SRC_FOLDER = os.path.join(DESKTOP, 'exemplo')
NEW_FOLDER = os.path.join(DESKTOP, 'new_folder')

# Criando uma nova pasta e verificando se ela já existe
os.makedirs(NEW_FOLDER, exist_ok=True)

# Listando os arquivos nas pastas
""" for root, dirs, files in os.walk(SRC_FOLDER):
    for dir_ in dirs:
        # Criando a nova pasta e copiando os diretórios para outra pasta
        new_directory_path = os.path.join(
            root.replace(SRC_FOLDER, NEW_FOLDER), dir_ 
        )
        print(new_directory_path)
        os.makedirs(new_directory_path, exist_ok=True)

    for file in files:
        path_file = os.path.join(root, file)
        new_file_path = os.path.join(
            root.replace(SRC_FOLDER, NEW_FOLDER), file
        )
        shutil.copy(path_file, new_file_path)  """

# Outra maneira de fazer a copia de arquivos
shutil.copytree(SRC_FOLDER, NEW_FOLDER)

# Apagando uma pasta e tudo que há dentro dela
#shutil.rmtree(NEW_FOLDER)