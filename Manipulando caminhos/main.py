from pathlib import Path


caminho_atual = Path()

# criando um arquivo
arquivo_teste = Path('arquivo_teste.txt')
arquivo_teste.touch()  # cria um arquovo na raiz


arquivo = caminho_atual / 'arquivo'

# caminho absoluto
caminho_absoluto = arquivo.absolute()

















