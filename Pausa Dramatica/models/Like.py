import sqlite3


class PesquisarPontos:
    def __init__(self, tabela, id_pontoturistico, name, lugar):
        self.tabela = tabela
        self.id_pontoturistico = id_pontoturistico
        self.name = name
        self.lugar = lugar

    def pesquisa(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT name, descricao FROM pontos_turisticos WHERE lugar = ?''', (input_pesquisa))
        rows = cursor.fetchall()
        connection.close()
        return rows


class CriarPontos:
    def __init__(self, tabela, id_pontoturistico, name, descricao, lugar):
        self.tabela = tabela
        self.id_pontoturistico = id_pontoturistico
        self.name = name
        self.descricao = descricao
        self.lugar = lugar

    def criar(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT name FROM pontos_turisticos WHERE name = ?''', (input_name))
        rows = cursor.fetchall()
        connection.close()
        if(rows == []):
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO pontos_turisticos(name, descricao, lugar) VALUES (?, ?, ?)''', (input_name, input_descricao, input_lugar))
            connection.commit()
            connection.close()


class LikePontos:
    def __init__(self, tabela, id_pontoturistico, id_usuario, data, avaliacao):
        self.tabela = tabela
        self.id_pontoturistico = id_pontoturistico
        self.id_usuario = id_usuario
        self.data = data
        self.avaliacao = avaliacao
    
    def save(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO {}(id_pontoturistico, id_usuario, data, avaliacao) VALUES(?, ?, ?, ?)'''.format(self.tabela), (self.id_pontoturistico, self.id_usuario, self.data, self.avaliacao))
        connection.commit()
        connection.close()

    def get_all(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        cursor.execute('''SELECT * FROM {}'''.format(self.tabela))
        rows = cursor.fetchall()

        return rows
    def get(self, **kwargs):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        for item in kwargs.keys():
            cursor.execute('''SELECT * FROM {} WHERE {}=?'''.format(self.tabela, item), (kwargs[item]))
            rows = cursor.fetchall()
            return rows

