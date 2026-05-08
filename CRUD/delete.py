def deletar_aluno(matricula):
  conn = conectar()
  cursor = conn.cursor()

  cursor.execute("""
  DELETE FROM alunos WHERE matricula = ?
  """, (matricula,))

  conn.commit()
  conn.close()
