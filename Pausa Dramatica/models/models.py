import sqlite3

class Model:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def save(self):
        query = '''INSERT INTO {}('''.format(self.tabela)
        part = ') VALUES('
        for item in self.__dict__.keys():
            if not item == list(self.__dict__.keys())[0]:
                if item == list(self.__dict__.keys())[1]:
                    query += item
                    if type(self.__dict__[item]) == str:
                        part += '"' + str(self.__dict__[item]) + '"'
                    else:
                        part += '' + str(self.__dict__[item])
                else:
                    if type(self.__dict__[item]) == str:
                        part += ', ' + '"' + str(self.__dict__[item]) + '"'
                    else:
                        part += ', ' + str(self.__dict__[item])
                    query += ', ' + item
        query += part + ')'
        print(query)

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def get_all(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        cursor.execute('''SELECT * FROM {}'''.format(self.tabela))
        rows = cursor.fetchall()
        connection.close()
        return rows

    def get(self, **kwargs):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        for item in kwargs.keys():
            cursor.execute('''SELECT * FROM {} WHERE {}=?'''.format(self.tabela, item), [kwargs[item]])
            rows = cursor.fetchall()
            return rows