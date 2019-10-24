import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute(
'''
CREATE TABLE IF NOT EXISTS Passeios(
    id_passeio INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_guia INTEGER NOT NULL,
    nome TEXT NOT NULL,
    local TEXT NOT NULL,
    vagas INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    avaliacao VARCHAR NOT NULL,
    FOREIGN KEY (id_guia) REFERENCES Usuarios(id),
    FOREIGN KEY (local) REFERENCES  ponto_turistico(lugar)
)
'''
)

class PesquisarPasseios:
    def __init__(self, Passeios, id_passeio, nome, local, vagas, descricao):
        self.Passeios = Passeios
        self.nome = nome
        self.id_passeio = id_passeio
        self.local = local
        self.vagas = vagas
        self.descricao = descricao

    def pesquisa(self):
        connection = sqlite3.connect('Passeios.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT nome, vagas, descricao FROM Passeios WHERE local = ?''', (input_pesquisa))
        rows = cursor.fetchall()
        connection.close()
        return rows


class CriarPasseios:
    def __init__(self, Passeios, id_passeio, nome, descricao):
        self.Passeios = Passeios
        self.id_passeio = id_passeio
        self.nome = nome
        self.descricao = descricao

    def criar(self):
        connection = sqlite3.connect('Passeios.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT nome FROM Passeios WHERE nome = ?''', (input_nome))
        rows = cursor.fetchall()
        connection.close()
        if(rows == []):
            connection = sqlite3.connect('Passeios.db')
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Passeios(nome, vagas, descricao) VALUES (?, ?, ?)''', (input_nome, input_vagas, input_descricao))
            connection.commit()
            connection.close()


class LikePontos:
    def __init__(self, Passeios, id_passeio, id_guia, avaliacao):
        self.Passeios = Passeios
        self.id_passeio = id_passeio
        self.id_guia = id_guia
        self.avaliacao = avaliacao
    
    def save(self):
        connection = sqlite3.connect('Passeios.db')
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO {}(id_passeio, id_guia, avaliacao) VALUES(?, ?, ?)'''.format(self.Passeios), (self.id_passeio, self.id_guia, self.avaliacao))
        connection.commit()
        connection.close()

    def get_all(self):
        connection = sqlite3.connect('Passeios.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM {}'''.format(self.Passeios))
        rows = cursor.fetchall()
        return rows

    def get(self, **kwargs):
        connection = sqlite3.connect('Passeios.db')
        cursor = connection.cursor()
        for item in kwargs.keys():
            cursor.execute('''SELECT * FROM {} WHERE {}=?'''.format(self.Passeios, item), (kwargs[item]))
            rows = cursor.fetchall()
            return rows

