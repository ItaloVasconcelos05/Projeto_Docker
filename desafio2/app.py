import sqlite3

conn = sqlite3.connect("data/banco.db")
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS pessoas (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')

cur.execute('INSERT INTO pessoas (nome, idade) VALUES ("Usuário xxx", 25)')

conn.commit()

cur.execute('SELECT * FROM pessoas')
print(cur.fetchall(), flush=True)

conn.close()