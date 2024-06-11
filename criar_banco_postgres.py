import psycopg2
from psycopg2 import Error

try:
    # Conecta ao PostgreSQL (substitua os valores pelos seus próprios)
    connection = psycopg2.connect(user="seu_usuario",
                                  password="sua_senha",
                                  host="localhost",
                                  port="5432",
                                  database="seu_banco_de_dados")

    cursor = connection.cursor()

    # Cria a tabela "usuarios" com colunas para nome e email
    create_table_query = '''CREATE TABLE usuarios
                (id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT NOT NULL); '''
    cursor.execute(create_table_query)
    connection.commit()

    # Insere alguns dados de exemplo na tabela
    insert_query = """ INSERT INTO usuarios (nome, email) VALUES (%s,%s)"""
    values = [("João", "joao@example.com"),
              ("Maria", "maria@example.com")]
    cursor.executemany(insert_query, values)
    connection.commit()

    print("Tabela de usuários criada e dados inseridos com sucesso.")

except (Exception, Error) as error:
    print("Erro ao trabalhar com o PostgreSQL:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexão ao PostgreSQL fechada.")
