""" 
    A pathlib normalmente é usada para trabalhar com caminhos, pastas e arquivos de forma que um código funcione em todos os SOs.
    A pathlib retorna um novo objeto dela
"""

from pathlib import Path
import os

os.system('cls')

path = Path()  # Trabalha com o caminho relativo.

print(path.absolute())  # Trabalhando com caminho absoluto.

file_path = Path(__file__)  # Obtendo o caminho do arquivo atual

print(file_path)

print(file_path.parent)  # Obtendo o caminho do diretório do arquivo

print(Path.home() / 'Desktop' / 'arq.txt')  # Obtendo a home do usuário

file = Path.home() / 'Desktop' / 'arq.txt'  #  Criando um caminho sem criá-lo do sistema
# file.touch(file)  #  Executa o caminho criado

# file.write_text("Texto")  # Escrevendo texto no arquivo (sobrescreve)

# print(file.read_text())  # Lendo o arquivo

# file.unlink() # Apaga o arquivo criado

folder = Path.home() / 'Desktop' / 'Folder'
folder.mkdir()  #  Cria um diretório
folder.mkdir(exist_ok=True)  #  Se já existir, não da erro

# folder.rmdir  # Apaga o diretório vazio

# Criando vários arquivos de uma vez

files = file_path / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    #file.touch()

    #if file.is_file():  # Verifica se é um arquivo

    #if file.is_dir():  # Verifica se é um diretório  
    
    if file.exists():  # Verifica se o arq/dir já existe
        file.unlink()  # Caso exista, ele será apagado
    else:
        file.touch()

    
    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')