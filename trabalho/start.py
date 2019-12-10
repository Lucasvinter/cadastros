from flask import Flask, render_template, redirect, request, url_for
from conexao import conn, cursor
from funcionario import Funcionario
from pessoa import Pessoa
from funcoesbd import *

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
    lista = Funcao()
    lista.listar()
    return render_template('listagem.html', nome = nome_template, empregado = lista.listar())

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    data_nascimento = request.form['data_nascimento']
    sexo = request.form['sexo']
    cargo = request.form['cargo']
    salario = request.form['salario']
    carga_horaria = request.form['carga_horaria']
    cadastra = Funcao()
    cadastra.cadastrar(nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria)
    return redirect('/listagem')


@app.route('/update', methods=['POST'])
def update():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    data_nascimento = request.form['data_nascimento']
    sexo = request.form['sexo']
    cargo = request.form['cargo']
    salario = request.form['salario']
    carga_horaria = request.form['carga_horaria']
    id = int(request.form['id'])
    altera = Funcao()
    altera.alterar(nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria, id)
    return redirect('/listagem')

@app.route('/excluir', methods=['POST'])
def excluir():
    id = request.form['excluir']
    deleta = Funcao()
    deleta.deletar(id)
    return redirect('/listagem')    

@app.route('/editar', methods=['POST'])
def editar():
    lista = []
    id = request.form['editar']
    cursor.execute("SELECT * FROM funcionarios WHERE id = {}".format(id))
    for linha in cursor.fetchall():
        person = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
        lista.append(person)
    return render_template('editar_funcionario.html', nome = nome_template, empregado = lista)

@app.route('/buscar_id', methods=['POST'])
def buscar_id():
    id = request.form['buscaID']
    buscaid = Funcao()
    if id != '':
        buscaid.filtro_id(id)
        return render_template('listagem.html', nome = nome_template, empregado = buscaid.filtro_id(id))
    else:
        buscaid.listar()
        return render_template('listagem.html', nome = nome_template, empregado = buscaid.listar())

@app.route('/buscar_nome', methods=['POST'])
def buscar_nome():
    nome = str(request.form['buscaNome'])
    buscanome = Funcao()
    if nome != '':
        buscanome.filtro_nome(nome)
        return render_template('listagem.html', nome = nome_template, empregado = buscanome.filtro_nome(nome))
    else:
        buscanome.listar()
        return render_template('listagem.html', nome = nome_template, empregado = buscanome.listar())


app.run(debug=True)