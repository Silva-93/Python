"""
    CSV -> Comma Separated Values
    É um formato de arquivo que armazena dados em forma de tabela, onde cada linha representa uma linha da tabela e as colunas são representadas por vírgulas. É amplamente utilizado para transferir dados entre sistemas de diferentes plataformas, como importar e exportar dados para uma planilha ou para uma base de dados. Este arquivo tem a extensão ".csv" e pode ser aberto em um editor de texto ou uma planilha eletrônica. Um exemplo de um arquivo CSV
    
    Nome,Idade,Endereço
    Luiz,32,"Av Brasil,21,centro"

    A primeiro linha do arquivo define os nomes das colunas enquanto as linhas seguintes contêm os valores das linhas separados por vírgulas.

    Regras
    1- Separe os valores das colunas com um delimitador único (,).
    2- Cada registro deve estar em uma linha.
    3- Não deixe linhas ou espaços sobrando.
    4- Use o caracter de escape ("") quando o delimitador aparecer no valor.

"""

# Lendo um arquivo CSV

# csv.reader -> Lê o CSV no formato de lista
# csv.DictReader -> Lê o CSV no formato dicionário

from pathlib import Path
import csv
import os
os.system('cls')

#  Pegando o cominho do arquivo
PATH_CSV = Path(__file__).parent / 'arq-csv.csv'
print(PATH_CSV)

""" with open(PATH_CSV, 'r') as arquivo:
    reader = csv.reader(arquivo)

    # Lendo os dados do arquivo
    for row in reader:
        print(row)  # Lendo os dados do arquivo

        # Lendo os dados do arquivo pelo índice
        print(row[0])  
        print(row[1])
        print(row[2]) """

    # Lendo em formato de dicionário
""" with open(PATH_CSV, 'r') as arquivo:
    reader = csv.DictReader(arquivo)

    # Lendo os dados do arquivo
    for row in reader:
        print(row)  # Lendo os dados do arquivo
        
        # Lendo os dados do arquivo pelas colunas
        print(row['Nome'])
        print(row['Idade'])
        print(row['Endereco']) """

# Escrevendo em arquivos CSV

customers_list = [
    {'Nome': 'Jouber Vicente', 'Idade': '29', 'Endereco': 'Av Sebastiao Salazar, N 600'},
    {'Nome': 'Ricardo Andrade', 'Idade': '42', 'Endereco': 'Rua Neves, N 34'},
    {'Nome': 'Maria Leila', 'Idade': '25', 'Endereco': 'Rua 12, N 6'},
]

PATH_CSVW = Path(__file__).parent / 'arq-csvW.csv'

""" with open(PATH_CSVW, 'w') as file:
    columns = customers_list[0].keys()  # Selecionando as colunas do arquivo
    reader = csv.writer(file)
    reader.writerow(columns)  # Adicionando o nome das colunas no csv

    for customers in customers_list:
        reader.writerow(customers.values())  # Adicionando os valores no CSV no formato de listas """

#  Adicionando valores no formato de dicionário

with open(PATH_CSVW, 'w') as file:
    columns = customers_list[0].keys()  # Selecionando as colunas do arquivo
    reader = csv.DictWriter(
        file,
        fieldnames=columns 
    )
    reader.writeheader()  # Escrevendo o cabeçalho

    for customers in customers_list:
        print(customers)
        reader.writerow(customers)