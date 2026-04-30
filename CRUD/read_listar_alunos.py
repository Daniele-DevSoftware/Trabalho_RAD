def listar_alunos():
  conn = conectar()
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM alunos")
  alunos = cursor.fetchall()

  conn.close()
  return alunos
