""" 
    A pathlib normalmente é usada para trabalhar com caminhos, pastas e arquivos de forma que um código funcione em todos os SOs.
"""

from pathlib import Path

path = Path()  # Trabalha com o caminho relativo.

print(path.absolute())  # Trabalhando com caminho absoluto.

