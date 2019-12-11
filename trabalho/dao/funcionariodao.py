from model.funcionario import Funcionario
from dao.conexao import Conexao

class FuncionarioDao(Conexao):
    #--- Método para cadastrar um funcionario
    def cadastrar_func(self, funcionario:Funcionario):
        self.cursor.execute("INSERT INTO funcionarios VALUES (DEFAULT, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(funcionario.get_nome(), funcionario.get_sobrenome(), funcionario.get_cpf(), funcionario.get_data_nascimento(), funcionario.get_sexo(), funcionario.get_cargo(), funcionario.get_salario(), funcionario.get_carga_horaria()))
        self.conn.commit()
    
    #--- Método para alterar um funcionario --- 
    def alterar_func(self, funcionario:Funcionario):
        self.cursor.execute("UPDATE funcionarios SET nome = '{}', sobrenome = '{}', cpf = '{}', data_nascimento = '{}', sexo = '{}', cargo = '{}', salario = '{}', carga_horaria = '{}' WHERE id = {}".format(funcionario.get_nome(), funcionario.get_sobrenome(), funcionario.get_cpf(), funcionario.get_data_nascimento(), funcionario.get_sexo(), funcionario.get_cargo(), funcionario.get_salario(), funcionario.get_carga_horaria(), funcionario.get_id()))
        self.conn.commit()
    
    
    #--- Método para listar todos os funcionarios cadastradas
    def listar_func(self):   
        lista = []
        self.cursor.execute("SELECT * FROM funcionarios")
        self.conn.commit()
        for linha in self.cursor.fetchall():
            people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(people)
        return lista
    
    
    #--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
    def deletar_func(self, id):
        self.cursor.execute("DELETE FROM funcionarios WHERE id = {}".format(id))
        self.conn.commit()
    
    #--- Metodo para filtrar uma funcionarios pelo 'Id' na lista de funcionarios cadastradas
    def filtro_id_func(self, id):
        lista = []
        self.cursor.execute("SELECT * FROM funcionarios WHERE id = {}".format(id))
        self.conn.commit()
        for linha in self.cursor.fetchall():
            people = people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(people)
        return lista
    
    
    #--- Método para filtrar funcionario por 'nome' na lista de funcionarios cadastradas
    def filtro_nome_func(self, nome):
        lista = []
        self.cursor.execute("SELECT * FROM funcionarios WHERE nome = '{}'".format(nome))
        self.conn.commit()
        for linha in self.cursor.fetchall():
            people = people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(people)
        return lista


    def editar_func(self, id):
        lista = []    
        self.cursor.execute("SELECT * FROM funcionarios WHERE id = {}".format(id))
        for linha in self.cursor.fetchall():
            person = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(person)
        return lista    