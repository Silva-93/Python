"""     Cliente MySQL

    PyMySQL -> Um cliente MySQL feito em python puro
    pip install pymysql
"""

import pymysql
import dotenv
import os

dotenv.load_dotenv()

# conexão com a base de dados
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],  # Servidor que será conectado
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS customers ('
                'id INT NOT NULL AUTO_INCREMENT, '
                'nome VARCHAR(50) NOT NULL, '
                'idade INT NOT NULL, '
                'PRIMARY KEY (id) '
            ')'
        )
        print(cursor)
