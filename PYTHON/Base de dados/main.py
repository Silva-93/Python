import sqlite3
from pathlib import Path

# Caminhos e nomes do arquivo 
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()  # cursor é o vai gerenciar a base de dados






# Criando uma tabela e adicionando colunas
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'    
    ')'
)
connection.commit()

# Inserindo valores nas colunas e colocando mais segurança ou "?" dificultão a ação do SQL injection
sql = (f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ? )')
# cursor.execute(sql, ['Jouber', 80])

# cursor.executemany(sql, (
#     ('Jouber', 80),
#     ('Maria', 62), 
#     ('Carlos', 95),
#     ('Renata', 72),
#     ('Fernando', 65),
#     ('Laura', 56)
# ))  # executa mais de um comando SQL

# connection.commit()

cursor.execute(f'UPDATE {TABLE_NAME} SET "name"="Larissa" WHERE id = 61')
connection.commit()

cursor.execute(f'UPDATE {TABLE_NAME} SET "weight"="88" WHERE id = 58')
connection.commit()


if __name__ == '__main__':
    print(sql)

    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = "60"')
    connection.commit()


    cursor.close()
    connection.close()

