from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BC = PASTA_ORIGINAIS / 'R20230901.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BC)
# writer = PdfWriter()

page1 = reader.pages[0]

#  Separando páginas do pdf
# writer.add_page(page1)

# with open(PASTA_NOVA / 'page1.pdf', 'wb') as arquivo:
#     writer.write(arquivo)

# gereando um novo pdf com as mesmas paginas do original
# with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as arquivo:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(arquivo)

# Criando vários pdfs a partir de um com várias páginas, cada página será um PDF
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'pdf{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)