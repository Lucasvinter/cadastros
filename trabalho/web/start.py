import sys
sys.path.append('C:/Users/55479/Desktop/TrabalhoPronto/cadastros/trabalho/')
from flask import Flask, render_template, redirect, request, url_for
from dao.conexao import Conexao
from dao.funcionariodao import FuncionarioDao
from dao.linguagemdao import LinguagemDao
from dao.equipesdao import EquipesDao
from model.equipes import Equipes
from model.funcionario import Funcionario
from model.linguagem import Linguagem
from model.pessoa import Pessoa

app = Flask(__name__)
nome_template = 'HBSIS'

@app.route('/')
def index():
    return render_template('layout.html', nome = nome_template)

@app.route('/formulario_func')
def formulario_func():
    return render_template('formulario_func.html', nome = nome_template)

@app.route('/listagem_func')
def listagem_func():
    lista = FuncionarioDao()
    lista.listar_func()
    return render_template('listagem_func.html', nome = nome_template, empregado = lista.listar_func())

@app.route('/salvar_func', methods=['POST'])
def salvar_func():
    nome = request.form['nome']
    sobre_nome = request.form['sobrenome']
    cpf = request.form['cpf']
    data_nascimento = request.form['data_nascimento']
    sexo = request.form['sexo']
    cargo = request.form['cargo']
    salario = request.form['salario']
    carga_horaria = request.form['carga_horaria']
    cadastra = FuncionarioDao()
    cadastra.cadastrar_func(Funcionario(nome, sobre_nome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria))
    return redirect('/listagem_func')


@app.route('/update_func', methods=['POST'])
def update_func():
    nome = request.form['nome']
    sobre_nome = request.form['sobrenome']
    cpf = request.form['cpf']
    data_nascimento = request.form['data_nascimento']
    sexo = request.form['sexo']
    cargo = request.form['cargo']
    salario = request.form['salario']
    carga_horaria = request.form['carga_horaria']
    id = int(request.form['id'])
    altera = FuncionarioDao()
    altera.alterar_func(Funcionario(nome, sobre_nome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria, id))
    return redirect('/listagem_func')

@app.route('/excluir_func', methods=['POST'])
def excluir_func():
    id = request.form['excluir']
    deleta = FuncionarioDao()
    deleta.deletar_func(id) 
    return redirect('/listagem_func')   

@app.route('/editar_func', methods=['POST'])
def editar_func():  
    id = int(request.form['editar'])
    edita = FuncionarioDao()
    editar = edita.editar_func(id)
    return render_template('editar_funcionario.html', nome = nome_template, empregado = editar)

@app.route('/buscar_id_func', methods=['POST'])
def buscar_id_func():
    id = int(request.form['buscaID'])
    buscaid = FuncionarioDao()
    if id != '':
        buscaid.filtro_id_func(id)
        return render_template('listagem_func.html', nome = nome_template, empregado = buscaid.filtro_id_func(id))
    else:
        buscaid.listar_func()
        return render_template('listagem_func.html', nome = nome_template, empregado = buscaid.listar_func())

@app.route('/buscar_nome_func', methods=['POST'])
def buscar_nome_func():
    nome = str(request.form['buscaNome'])
    buscanome = FuncionarioDao()
    if nome != '':
        buscanome.filtro_nome_func(nome)
        return render_template('listagem_func.html', nome = nome_template, empregado = buscanome.filtro_nome_func(nome))
    else:
        buscanome.listar_func()
        return render_template('listagem_func.html', nome = nome_template, empregado = buscanome.listar_func())


@app.route('/formulario_equipe')
def formulario_equipe():
    return render_template('formulario_equipe.html', nome = nome_template)

@app.route('/listagem_equipe')
def listagem_equipe():
    lista = EquipesDao()
    lista.listar_equipe()
    return render_template('listagem_equipe.html', nome = nome_template, empregado = lista.listar_equipe())

@app.route('/salvar_equipe', methods=['POST'])
def salvar_equipe():
    nome = request.form['nome']
    lingua = request.form['linguagem']
    projeto = request.form['projeto']
    lider = request.form['lider']
    integrante1 = request.form['integrante1']
    integrante2 = request.form['integrante2']
    integrante3 = request.form['integrante3']
    integrante4 = request.form['integrante4']
    cadastra = EquipesDao()
    cadastra.cadastrar_equipe(Equipes(nome, lingua, projeto, lider, integrante1, integrante2, integrante3, integrante4))
    return redirect('/listagem_equipe')


@app.route('/update_equipe', methods=['POST'])
def update_equipe():
    nome = request.form['nome']
    lingua = request.form['linguagem']
    projeto = request.form['projeto']
    lider = request.form['lider']
    integrante1 = request.form['integrante1']
    integrante2 = request.form['integrante2']
    integrante3 = request.form['integrante3']
    integrante4 = request.form['integrante4']
    id = int(request.form['id'])
    altera = EquipesDao()
    altera.alterar_equipe(Equipes(nome, lingua, projeto, lider, integrante1, integrante2, integrante3, integrante4, id))
    return redirect('/listagem_equipe')

@app.route('/excluir_equipe', methods=['POST'])
def excluir_equipe():
    id = request.form['excluir']
    deleta = EquipesDao()
    deleta.deletar_equipe(id)
    return redirect('/listagem_equipe')    

@app.route('/editar_equipe', methods=['POST'])
def editar_equipe():
    id = int(request.form['editar'])
    edita = EquipesDao()
    editar = edita.editar_equipe(id)
    return render_template('editar_equipe.html', nome = nome_template, empregado = editar)

@app.route('/buscar_id_equipe', methods=['POST'])
def buscar_id_equipe():
    id = int(request.form['buscaID'])
    buscaid = EquipesDao()
    if id != '':
        buscaid.filtro_id_equipe(id)
        return render_template('listagem_equipe.html', nome = nome_template, empregado = buscaid.filtro_id_equipe(id))
    else:
        buscaid.listar_equipe()
        return render_template('listagem_equipe.html', nome = nome_template, empregado = buscaid.listar_equipe())

@app.route('/buscar_nome_equipe', methods=['POST'])
def buscar_nome_equipe():
    nome = str(request.form['buscaNome'])
    buscanome = EquipesDao()
    if nome != '':
        buscanome.filtro_nome_equipe(nome)
        return render_template('listagem_equipe.html', nome = nome_template, empregado = buscanome.filtro_nome_equipe(nome))
    else:
        buscanome.listar_equipe()
        return render_template('listagem_equipe.html', nome = nome_template, empregado = buscanome.listar_equipe())


@app.route('/formulario_ling')
def formulario_ling():
    return render_template('formulario_linguagem.html', nome = nome_template)

@app.route('/listagem_ling')
def listagem_ling():
    lista = LinguagemDao()
    lista.listar_ling()
    return render_template('listagem_linguagem.html', nome = nome_template, empregado = lista.listar_ling())

@app.route('/salvar_ling', methods=['POST'])
def salvar_ling():
    nome = request.form['nome']
    desc = request.form['descricao']
    cadastra = LinguagemDao()
    cadastra.cadastrar_ling(Linguagem(nome, desc))
    return redirect('/listagem_ling')


@app.route('/update_ling', methods=['POST'])
def update_ling():
    nome_ling = request.form['nome']
    desc = request.form['descricao']
    id = int(request.form['id'])
    altera = LinguagemDao()
    altera.alterar_ling(Linguagem(nome_ling, desc, id))
    return redirect('/listagem_ling')

@app.route('/excluir_ling', methods=['POST'])
def excluir_ling():
    id = request.form['excluir']
    deleta = LinguagemDao()
    deleta.deletar_ling(id)
    return redirect('/listagem_ling')    

@app.route('/editar_ling', methods=['POST'])
def editar_ling():
    id = int(request.form['editar'])
    edita = LinguagemDao()
    editar = edita.editar_ling(id)
    return render_template('editar_linguagem.html', nome = nome_template, empregado = editar)

@app.route('/buscar_id_ling', methods=['POST'])
def buscar_id_ling():
    id = int(request.form['buscaID'])
    buscaid = LinguagemDao()
    if id != '':
        buscaid.filtro_id_ling(id)
        return render_template('listagem_linguagem.html', nome = nome_template, empregado = buscaid.filtro_id_ling(id))
    else:
        buscaid.listar_ling()
        return render_template('listagem_linguagem.html', nome = nome_template, empregado = buscaid.listar_ling())

@app.route('/buscar_nome_ling', methods=['POST'])
def buscar_nome_ling():
    nome = str(request.form['buscaNome'])
    buscanome = LinguagemDao()
    if nome != '':
        buscanome.filtro_nome_ling(nome)
        return render_template('listagem_linguagem.html', nome = nome_template, empregado = buscanome.filtro_nome_ling(nome))
    else:
        buscanome.listar_ling()
        return render_template('listagem_linguagem.html', nome = nome_template, empregado = buscanome.listar_ling())


app.run(debug=True)