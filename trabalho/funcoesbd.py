from conexao import conn, cursor

class Funcao:
    #--- Método para cadastrar um funcionario
    def cadastrar(self, nome, sobrenome, cpf:int, salario:int, cargo, carga_horaria, data_nascimento, sexo):
        cursor.execute("INSERT INTO funcionarios VALUES(DEFAULT, '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}')".format(salario, cargo, carga_horaria, nome, sobrenome, data_nascimento, cpf, sexo))
        conn.commit()
    
    
    #--- Método para alterar um funcionario --- 
    def alterar(self, nome, sobrenome, cpf:int, salario:int, cargo, carga_horaria:int, data_nascimento:int, sexo, id=int):
        cursor.execute("UPDATE funcionarios SET nome = '{}', sobrenome = '{}', cpf = {}, salario = {}, cargo = '{}', carga_horaria = {}, data_nascimento = {}, sexo = '{}' WHERE id = {}".format(nome, sobrenome, cpf, salario, cargo, carga_horaria, data_nascimento, sexo, id))
        conn.commit()
    
    
    #--- Método para listar todos os funcionarios cadastradas
    def listar(self):   
        lista = []
        cursor.execute("SELECT * FROM funcionarios")
        conn.commit()
        for linha in cursor.fetchall():
            people = {'salario': linha[0], 'id': linha[1], 'cargo': linha[2], 'carga_horaria': linha[3], 'nome': linha[4], 'sobrenome':linha[5], 'data_nascimento':linha[6], 'cpf':[7], 'sexo':[8]}
            lista.append(people)
        return lista
    
    
    #--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
    def deletar(self, id:int):
        cursor.execute("DELETE FROM funcionarios WHERE id = {}".format(id))
    
    
    #--- Metodo para filtrar uma funcionarios pelo 'Id' na lista de funcionarios cadastradas
    def filtro_id(self, id:int):
        lista = []
        cursor.execute("SELECT * FROM funcionarios WHERE id = {}".format(id))
        conn.commit()
        for linha in cursor.fetchall():
            people = {'salario': linha[0], 'id': linha[1], 'cargo': linha[2], 'carga_horaria': linha[3], 'nome': linha[4], 'sobrenome':linha[5], 'data_nascimento':linha[6], 'cpf':[7], 'sexo':[8]}
            lista.append(people)
        return lista
    
    
    #--- Método para filtrar funcionario por 'nome' na lista de funcionarios cadastradas
    def filtro_nome(self, nome:str):
        lista = []
        cursor.execute("SELECT * FROM funcionarios WHERE nome = '{}'".format(nome))
        conn.commit()
        for linha in cursor.fetchall():
            people = {'salario': linha[0], 'id': linha[1], 'cargo': linha[2], 'carga_horaria': linha[3], 'nome': linha[4], 'sobrenome':linha[5], 'data_nascimento':linha[6], 'cpf':[7], 'sexo':[8]}
            lista.append(people)
        return lista