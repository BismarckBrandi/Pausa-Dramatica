import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

#criar tabela
conn = sqlite3.connect('DADOS.db')
cursor = conn.cursor()
cursor.execute(
"""
  CREATE TABLE IF NOT EXISTS DADOS (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        locais TEXT NOT NULL
   )
""")

conn.close()
#inserir
conn = sqlite3.connect('DADOS.db')
cursor = conn.cursor()
cursor.execute("""
INSERT INTO DADOS (locais)
VALUES ('Rio de Janeiro')
""")
conn.commit()
conn.close()

#Buscar
def Pesquisa_local():
    db=str(request.form('banco de dados'))
    table=str(request.form('tabela'))
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    tabela=cursor.execute('select * from {0}'.format(table))
    conn.close()
    return tabela


app.run()