import sqlite3

# Conecta ao banco de dados (ou cria um novo se não existir)
conn = sqlite3.connect('usuarios.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria a tabela "usuarios" com colunas para nome e email
cursor.execute('''CREATE TABLE usuarios
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL)''')

# Insere alguns dados de exemplo na tabela
cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("João", "joao@example.com"))
cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("Maria", "maria@example.com"))

# Salva as alterações e fecha a conexão
conn.commit()
conn.close()
