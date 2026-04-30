def criar_tabela():
  conn = conectar()
  cursor = conn.cursor()

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS alunos (
    matricula TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    data_nascimento TEXT,
    nota REAL
  )
  """)

  conn.commit()
  conn.close()
