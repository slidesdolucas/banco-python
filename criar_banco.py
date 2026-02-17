import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    cpf TEXT,
    telefone TEXT
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")
