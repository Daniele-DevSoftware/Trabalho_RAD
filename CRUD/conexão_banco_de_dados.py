import sqlite 3
def conectar():
  return sqlite3.connect("alunos.db")
