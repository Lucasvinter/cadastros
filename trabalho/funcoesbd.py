from conexao import conn, cursor

class Funcao:
    #--- Método para cadastrar um funcionario
    def cadastrar(self, nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria, fk_equipes):
        cursor.execute("INSERT INTO funcionarios VALUES (DEFAULT, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria, fk_equipes))
        conn.commit()
    
    
    #--- Método para alterar um funcionario --- 
    def alterar(self, nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria, id):
        cursor.execute("UPDATE funcionarios SET nome = '{}', sobrenome = '{}', cpf = '{}', data_nascimento = '{}', sexo = '{}', cargo = '{}', salario = '{}', carga_horaria = '{}' WHERE id = '{}'".format(nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria, id))
        conn.commit()
    
    
    #--- Método para listar todos os funcionarios cadastradas
    def listar(self):   
        lista = []
        cursor.execute("SELECT * FROM funcionarios")
        conn.commit()
        for linha in cursor.fetchall():
            people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(people)
        return lista
    
    
    #--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
    def deletar(self, id):
        cursor.execute("DELETE FROM funcionarios WHERE id = {}".format(id))
    
    
    #--- Metodo para filtrar uma funcionarios pelo 'Id' na lista de funcionarios cadastradas
    def filtro_id(self, id):
        lista = []
        cursor.execute("SELECT * FROM funcionarios WHERE id = {}".format(id))
        conn.commit()
        for linha in cursor.fetchall():
            people = people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(people)
        return lista
    
    
    #--- Método para filtrar funcionario por 'nome' na lista de funcionarios cadastradas
    def filtro_nome(self, nome:str):
        lista = []
        cursor.execute("SELECT * FROM funcionarios WHERE nome = '{}'".format(nome))
        conn.commit()
        for linha in cursor.fetchall():
            people = people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(people)
        return lista