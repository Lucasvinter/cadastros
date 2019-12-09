from flask import Flask, render_template, redirect, request, url_for
from funcionario import Funcionario
from conexao import conn, cursor
from pessoa import *
import funcoesbd

app = Flask(__name__)
nome_template = 'HBSIS'

@app.route('/')
def index():
    return render_template('layout.html', nome = nome_template)

@app.route('/formulario')
def formulario():
    return render_template('formulario.html', nome = nome_template)

@app.route('/listagem')
def listagem():
    self.listar()
    return render_template('listagem.html', nome = nome_template, cliente = self.listar())

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    Pessoa(nome, sobrenome, cpf)
    cargo = request.form['cargo']
    salario = request.form['salario']
    carga_horaria = request.form['carga_horaria']
    Funcionario(salario, cargo, carga_horaria)
    self.cadastrar(nome, sobrenome, cpf)
    return redirect('/listagem')

@app.route('/excluir', methods=['POST'])
def excluir():
    id = request.form['excluir']
    self.deletar(id)
    return redirect('/listagem')

@app.route('/alterar', methods=['POST'] )
def alterar():
    lista = []
    id = request.form['editar']
    cursor.execute("SELECT * FROM clientes WHERE id = {}".format(id))
    for linha in cursor.fetchall():
        person = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3]}
        lista.append(person)
    return render_template('editar.html', nome = nome_template, cliente = lista)

@app.route('/buscar_id', methods=['POST'])
def buscar_id():
    id = int(request.form['buscaID'])
    if id == None:
        self.listar()
        return render_template('listagem.html', nome = nome_template, cliente = self.listar())
    else:
        self.filtro_id(id)
        return render_template('listagem.html', nome = nome_template, cliente = self.filtro_id(id))

@app.route('/buscar_nome', methods=['POST'])
def buscar_nome():
    nome = str(request.form['buscaNome'])
    if nome != '':
        self.filtro_nome(nome)
        return render_template('listagem.html', nome = nome_template, cliente = self.filtro_nome(nome))
    else:
        self.listar()
        return render_template('listagem.html', nome = nome_template, cliente = self.listar())


app.run()