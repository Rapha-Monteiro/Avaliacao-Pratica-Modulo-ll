"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""

import sqlite3
# 1) Criar banco de dados
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# 2) Criar tabela alunos'''

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    email TEXT NOT NULL
)
''')

print('Tabela criada com sucesso"\n')

# 3) Inserir registros
cursor.execute('INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)',
               ('José Lucas',18, 'Jose@gmail.com'))
cursor.execute('INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)',
               ('Ana Silva', 20, 'ana@gmail.com'))
cursor.execute('INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)',
               ('Carlos Souza', 22, 'carlos@gmail.com'))
cursor.execute('INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)',
               ('Mariana Dias', 19, 'maria@gmail.com'))
cursor.execute('INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)',
               ('Wellington',17, 'wellington@gmail.com'))
 
print("Dados inseridos!\n")

# 4) Listar todos os registros
print("Listando todos os alunos:")
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)
print()
# 5) Atualizar um registro
cursor.execute('UPDATE alunos SET email = ? WHERE nome = ?',
               ('jose.dev@gmail.com','José'))
conn.commit()
print('Após atualização do email do José:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# 6) Deletar um registro
cursor.execute('DELETE FROM alunos WHERE nome = ?',('Carlos Souza',))
conn.commit()

print('Após deletar do email do Carlos:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Encerrar conexão
conn.close()
