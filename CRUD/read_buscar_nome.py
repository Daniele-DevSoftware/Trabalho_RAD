def buscar_nome(matricula):
  conn = conectar()
  cursor = conn.cursor()

  cursor.execute("""
  SELECT * FROM alunos WHERE nome LIKE ?
  """, ('%' + nome + '%',))

  resultado = cursor.fetchall()

  conn.close()
  return resultado
