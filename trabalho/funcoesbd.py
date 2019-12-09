from conexao import conn, cursor

 #--- Método para cadastrar uma pessoa
def cadastrar(self, nome, sobrenome, cpf):
    cursor.execute("INSERT INTO funcionarios VALUES(DEFAULT, '{}', '{}', '{}')".format(nome, sobrenome, cpf))
    conn.commit()

#--- Método para alterar uma pessoa --- Ainda não implementado 
def alterar(self, nome, sobrenome, cpf, id=int):
    cursor.execute("UPDATE funcionarios SET nome = {}, sobrenome = {}, cpf = {} WHERE id = {}".format(nome, sobrenome, cpf, id))
    conn.commit()

#--- Método para listar todas as pessoas cadastradas
def listar(self):
    lista = []
    cursor.execute("SELECT * FROM funcionarios")
    conn.commit()
    for linha in cursor.fetchall():
        people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3]}
        lista.append(people)
    return lista

#--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
def deletar(self, id:int):
    cursor.execute("DELETE FROM funcionarios WHERE id = {}".format(id))

#--- Metodo para filtrar uma pessoa pelo 'Id' na lista de pessoas cadastradas
def filtro_id(self, id:int):
    lista = []
    cursor.execute("SELECT * FROM funcionarios WHERE id = {}".format(id))
    conn.commit()
    for linha in cursor.fetchall():
        people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3]}
        lista.append(people)
    return lista
    
#--- Método para filtrar pessoa por 'nome' na lista de pessoas cadastradas
def filtro_nome(self, nome:str):
    lista = []
    cursor.execute("SELECT * FROM funcionarios WHERE nome = '{}'".format(nome))
    conn.commit()
    for linha in cursor.fetchall():
        people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3]}
        lista.append(people)
    return lista