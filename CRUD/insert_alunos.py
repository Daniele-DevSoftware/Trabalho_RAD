def inserir_aluno(matricula, nome, data_nascimento, nota):
  conn = conectar()
  cursor = conn.cursor()

try:
  cursor.execute("""
  INSERT INTO alunos (matricula, nome, data_nasciemento, nota)
  VALUES (?, ?, ?, ?)
  """, (matricula, nome, data_nascimento, nota))

  conn.commit()
except sqlite3.IntegrityError:
  print("Matrícula já cadastrada!")

conn.close()
