import sqlite3
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()  # cursor é o vai gerenciar a base de dados

# Selecionando dados da base de dados
cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = "3"')

row = cursor.fetchone()
print(row)

# for row in cursor.fetchall():
#     _id, name, weight = row
#     print(_id, name, weight)


cursor.close()
connection.close()