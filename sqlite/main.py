import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Criar tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores na tabela
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome , :peso)'
)


# cursor.execute(sql, ['Joana', 4])
# cursor.executemany(
#     sql,
#     [
#         ['Mario', 4], ['Luiz', 8]
#     ]
# )
# cursor.execute(sql, {'nome': 'Wander', 'peso': 5})
cursor.executemany(sql, (
    {'nome': 'Lucio', 'peso': 3},
    {'nome': 'Lucia', 'peso': 1},
    {'nome': 'Roberto', 'peso': 3},
    {'nome': 'Caio', 'peso': 9},
    {'nome': 'felipi', 'peso': 5},
))
connection.commit()

# SQL

cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql)