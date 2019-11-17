from flask import Flask, render_template, request, redirect, url_for

from models.usuario import Usuario
from models.models import Model
from models.ponto_turistico import PontoTuristico
from models.passeio import Passeio

import sqlite3

app = Flask(__name__)

vLogin = 0
usr = ''
usrList = ''
"""
def pesquisar_pontos(pesquisa):
    global connection
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    #pesquisa = str(input("Digite o lugar para ver seus pontos turísticos: "))
    lista = cursor.execute(
    '''
    SELECT name, descricao FROM pontos_turisticos WHERE lugar = ''' + "'" + pesquisa + "'"
    ).fetchall()
    connection.close()
    return lista

def criar_pontos():
    global connection
    connection = sqlite3.connect('database.db')
    name = str(input("Digite o nome do ponto turistico: "))
    descricao = str(input("Digite a descricao do ponto turistico: "))
    lugar = str(input("Digite o lugar do ponto turistico: "))
    cursor = connection.cursor()
    lista = cursor.execute(
    '''
    SELECT name FROM pontos_turisticos WHERE name = ''' + "'" + name + "'"
    ).fetchall()
    connection.close()
    if(lista == []):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        lista = cursor.execute(
        '''
        INSERT INTO pontos_turisticos(name, descricao, lugar)
        VALUES ('''+"'"+name+"', "+"'"+descricao+"', "+"'"+lugar+"');"
        )
        connection.commit()
        connection.close()
        print("Ponto criado")
    else:
        print("Ja existe")
"""


@app.route('/')
def main():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    pontos = Model(tabela='pontos_turisticos')
    pts = pontos.get_all()
    print(pts)
    return render_template('index.html', len=len(pts), pontos= pts, vLogin=vLogin, usr= usr, usrList=usrList)

@app.route('/', methods = ['POST', 'GET'])
def search():
    local = request.form['Local']
    busca = Model(tabela='pontos_turisticos')
    resultado = busca.get(lugar=local)
    return render_template ('/Pesquisa local')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    global vLogin
    if vLogin == 0:
        if request.method == 'POST':
            username = request.form['username']
            senha = request.form['senha']

            user = Usuario(tabela='usuarios', username=username, senha=senha)
            validate = user.autenticar()

            if validate:
                #global vLogin
                global usr
                global usrList
                usr = username
                usuario = Model(tabela='usuarios')
                usrList = usuario.get(username=username)
                vLogin = 1
                return redirect(url_for('index'))
            else:
                return render_template('Login.html')
        if request.method == 'GET':
            return render_template('Login.html')
    else:
        #global vLogin
        vLogin = 0
        return redirect(url_for('index'))


@app.route('/registrar', methods = ['POST', 'GET'])
def registrar():
    if request.method == 'POST':
        username = request.form['username']
        senha = request.form['senha']
        email = request.form['email']
        tipo = request.form['tipo']

        user = Usuario(tabela='usuarios', username=username, senha=senha, email=email, tipo=tipo)
        validate = user.registrar()

        if validate:
            return redirect(url_for('login'))
        else:
            return render_template('registro.html')
    if request.method == 'GET':
        return render_template('registro.html')

@app.route('/criar', methods = ['POST', 'GET'])
def criar():
    if request.method == 'POST':
        name = request.form['name']
        descricao = request.form['descricao']
        lugar = request.form['lugar']

        user = PontoTuristico(tabela='pontos_turisticos', name=name, imagem="a", descricao=descricao, lugar=lugar)
        validate = user.criarPonto()  

        if validate:
            return redirect(url_for('index'))
        else:
            return render_template('criar.html')
    if request.method == 'GET':
        return render_template('criar.html')

@app.route('/<name>', methods = ['POST', 'GET'])
def ponto(name):
    ponto = Model(tabela='pontos_turisticos')
    pt = ponto.get(name=name)
    passeio = Model(tabela='passeios')
    dados = passeio.get(ponto=name)
    return render_template('ponto.html', len=len(dados), dados=dados, pontos= pt, vLogin=vLogin, usr= usr, usrList=usrList)

@app.route('/oferecer', methods = ['POST', 'GET'])
def oferecer():
    if request.method == 'POST':
        ponto = request.form['ponto']
        data = request.form['data']
        guia=usr

        user = Passeio(tabela='passeios', guia=guia, ponto=ponto, data=data)
        validate = user.oferecerPasseio()  

        if validate:
            return redirect(url_for('index'))
        else:
            return render_template('oferecer.html')
    if request.method == 'GET':
        return render_template('oferecer.html')

if __name__ == '__main__':
    app.run(debug=True)

