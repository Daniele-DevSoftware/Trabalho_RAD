def atualizar_aluno(matricula, nome, data_nascimento, nota):
  conn = conectar()
  cursor = conn.cursor()

  cursor.execute("""
  UPDATE alunos
  SET nome = ?, data_nascimento = ?, nota = ?
  WHERE matricula = ?
  """, (matricula, nome, data_nascimento, nota))

  conn.commit()
  conn.close()
