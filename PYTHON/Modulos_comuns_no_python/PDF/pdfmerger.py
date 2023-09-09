from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BC = PASTA_ORIGINAIS / 'R20230901.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BC)
writer = PdfWriter()
merger = PdfMerger()

page1 = reader.pages[0]

files = [PASTA_NOVA / 'pdf0.pdf', PASTA_NOVA / 'pdf1.pdf']

for file in files:
    merger.append(file)  

merger.write(PASTA_NOVA / 'MERGED.pdf')  
merger.close()
