"""     Cliente MySQL

    PyMySQL -> Um cliente MySQL feito em python puro
    pip install pymysql
"""

import pymysql

# conexão com a base de dados
connection = pymysql.connect(
    host='localhost',  # Servidor que será conectado
    user='usuario',
    password='senha',
    database='base_de_dados',
)

with connection:
    with connection.cursor() as cursor:
        ...
