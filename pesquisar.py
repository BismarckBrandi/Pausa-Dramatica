import sqlite3

#criar tabela
conn = sqlite3.connect('DADOS.db')
cursor = conn.cursor()
cursor.execute(
"""
  CREATE TABLE IF NOT EXISTS DADOS (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        locais TEXT NOT NULL,
        instancias TEXT NOT NULL
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
    db=input('banco de dados')
    user=input('usuario')
    table=input('tabela')
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    tabela=cursor.execute('select * from {0}.{1}'.format(user,table))
    conn.close()
    return tabela

'''def busca(path):
    dir(path)
    from index import
    pass

busca('C:\\Bismarck\\Prog\\flask\\')'''