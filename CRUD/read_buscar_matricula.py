def buscar_matricula(matricula):
  conn = conectar()
  cursor = conn.cursor()

  cursor.execute("""
  SELECT * FROM alunos WHERE matricula = ?
  """, (matricula,))

  aluno = cursor.fetchone()

  conn.close()
  return aluno
