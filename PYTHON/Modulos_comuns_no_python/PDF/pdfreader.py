# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
# pip install PyPDF2[image]

from pathlib import Path
from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BC = PASTA_ORIGINAIS / 'R20230901.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BC)

# sabendo a quantidade de páginas do pdf
# print(len(reader.pages))

# extraindo textos do pdf
page1 = reader.pages[0]  # página 1
# print(page1.extract_text())

# extraindo imagens do pdf
# print(len(page1.images))  # Sabendo o númerod e imagens do pdf
# print(page1.images[0])  # pegando a primeira imagem do pdf

# enviando imagem para um novo arquivo
imagem1 = page1.images[0]

with open(PASTA_NOVA / imagem1.name, 'wb') as fp:
    fp.write(imagem1.data)