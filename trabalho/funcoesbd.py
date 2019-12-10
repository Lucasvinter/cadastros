from conexao import conn, cursor
from funcionario import Funcionario
from linguagem import Linguagem
from equipes import Equipes



class Funcao:
    #--- Método para cadastrar um funcionario
    def cadastrar_func(self, funcionario:Funcionario):
        cursor.execute("INSERT INTO funcionarios VALUES (DEFAULT, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(funcionario.get_nome(), funcionario.get_sobrenome(), funcionario.get_cpf(), funcionario.get_data_nascimento(), funcionario.get_sexo(), funcionario.get_cargo(), funcionario.get_salario(), funcionario.get_carga_horaria()))
        conn.commit()
    
    #--- Método para alterar um funcionario --- 
    def alterar_func(self, funcionario:Funcionario):
        cursor.execute("UPDATE funcionarios SET nome = '{}', sobrenome = '{}', cpf = '{}', data_nascimento = '{}', sexo = '{}', cargo = '{}', salario = '{}', carga_horaria = '{}' WHERE id = {}".format(funcionario.get_nome(), funcionario.get_sobrenome(), funcionario.get_cpf(), funcionario.get_data_nascimento(), funcionario.get_sexo(), funcionario.get_cargo(), funcionario.get_salario(), funcionario.get_carga_horaria(), funcionario.get_id()))
        conn.commit()
    
    
    #--- Método para listar todos os funcionarios cadastradas
    def listar_func(self):   
        lista = []
        cursor.execute("SELECT * FROM funcionarios")
        conn.commit()
        for linha in cursor.fetchall():
            people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(people)
        return lista
    
    
    #--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
    def deletar_func(self, id):
        cursor.execute("DELETE FROM funcionarios WHERE id = {}".format(id))
    
    
    #--- Metodo para filtrar uma funcionarios pelo 'Id' na lista de funcionarios cadastradas
    def filtro_id_func(self, id):
        lista = []
        cursor.execute("SELECT * FROM funcionarios WHERE id = {}".format(id))
        conn.commit()
        for linha in cursor.fetchall():
            people = people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(people)
        return lista
    
    
    #--- Método para filtrar funcionario por 'nome' na lista de funcionarios cadastradas
    def filtro_nome_func(self, nome:str):
        lista = []
        cursor.execute("SELECT * FROM funcionarios WHERE nome = '{}'".format(nome))
        conn.commit()
        for linha in cursor.fetchall():
            people = people = {'id': linha[0], 'nome': linha[1], 'sobrenome': linha[2], 'cpf': linha[3], 'data_nascimento': linha[4], 'sexo': linha[5], 'cargo': linha[6], 'salario': linha[7], 'carga_horaria': linha[8]}
            lista.append(people)
        return lista

     #--- Método para cadastrar um funcionario
    def cadastrar_equipe(self, equipes:Equipes):
        cursor.execute("INSERT INTO equipes VALUES (DEFAULT, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(equipes.get_nome(), equipes.get_linguagem(), equipes.get_projeto(), equipes.get_lider(), equipes.get_integrante1(), equipes.get_integrante2(), equipes.get_integrante3(), equipes.get_integrante4()))
        conn.commit()
    
    
    #--- Método para alterar um funcionario --- 
    def alterar_equipe(self, equipes:Equipes):
        cursor.execute("UPDATE equipes SET nome = '{}', linguagem = '{}', projeto = '{}', lider = '{}', integrante1 = '{}', integrante2 = '{}', integrante3 = '{}', integrante4 = '{}' WHERE id = {}".format(equipes.get_nome(), equipes.get_linguagem(), equipes.get_projeto(), equipes.get_lider(), equipes.get_integrante1(), equipes.get_integrante2(), equipes.get_integrante3(), equipes.get_integrante4(), equipes.get_id()))
        conn.commit()
    
    
    #--- Método para listar todos os equipes cadastradas
    def listar_equipe(self):   
        lista = []
        cursor.execute("SELECT * FROM equipes")
        conn.commit()
        for linha in cursor.fetchall():
            equip = {'id': linha[0], 'nome': linha[1], 'linguagem': linha[2], 'projeto': linha[3], 'lider': linha[4], 'integrante1': linha[5], 'integrante2': linha[6], 'integrante3': linha[7], 'integrante4': linha[8]}
            lista.append(equip)
        return lista
    
    
    #--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
    def deletar_equipe(self, id):
        cursor.execute("DELETE FROM equipes WHERE id = {}".format(id))
    
    
    #--- Metodo para filtrar uma equipes pelo 'Id' na lista de equipes cadastradas
    def filtro_id_equipe(self, id):
        lista = []
        cursor.execute("SELECT * FROM equipes WHERE id = {}".format(id))
        conn.commit()
        for linha in cursor.fetchall():
            equip = equip = {'id': linha[0], 'nome': linha[1], 'linguagem': linha[2], 'projeto': linha[3], 'lider': linha[4], 'integrante1': linha[5], 'integrante2': linha[6], 'integrante3': linha[7], 'integrante4': linha[8]}
            lista.append(equip)
        return lista
    
    
    #--- Método para filtrar funcionario por 'nome' na lista de equipes cadastradas
    def filtro_nome_equipe(self, nome:str):
        lista = []
        cursor.execute("SELECT * FROM equipes WHERE nome = '{}'".format(nome))
        conn.commit()
        for linha in cursor.fetchall():
            equip = equip = {'id': linha[0], 'nome': linha[1], 'linguagem': linha[2], 'projeto': linha[3], 'lider': linha[4], 'integrante1': linha[5], 'integrante2': linha[6], 'integrante3': linha[7], 'integrante4': linha[8]}
            lista.append(equip)
        return lista

     #--- Método para cadastrar um funcionario
    def cadastrar_ling(self, linguagem:Linguagem):
        cursor.execute("INSERT INTO linguagem VALUES (DEFAULT, '{}', '{}')".format(linguagem.get_nome(), linguagem.get_descricao()))
        conn.commit()
    
    
    #--- Método para alterar um funcionario --- 
    def alterar_ling(self, linguagem:Linguagem):
        cursor.execute("UPDATE linguagem SET nome = '{}', descricao = '{}' WHERE id = {}".format(linguagem.get_nome(), linguagem.get_descricao(), linguagem.get_id()))
        conn.commit()
    
    
    #--- Método para listar todos os linguagem cadastradas
    def listar_ling(self):   
        lista = []
        cursor.execute("SELECT * FROM linguagem")
        conn.commit()
        for linha in cursor.fetchall():
            equip = {'id': linha[0], 'nome': linha[1], 'descricao': linha[2]}
            lista.append(equip)
        return lista
    
    
    #--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
    def deletar_ling(self, id):
        cursor.execute("DELETE FROM linguagem WHERE id = {}".format(id))
    
    
    #--- Metodo para filtrar uma linguagem pelo 'Id' na lista de linguagem cadastradas
    def filtro_id_ling(self, id):
        lista = []
        cursor.execute("SELECT * FROM linguagem WHERE id = {}".format(id))
        conn.commit()
        for linha in cursor.fetchall():
            equip = equip = {'id': linha[0], 'nome': linha[1], 'descricao': linha[2]}
            lista.append(equip)
        return lista
    
    
    #--- Método para filtrar funcionario por 'nome' na lista de linguagem cadastradas
    def filtro_nome_ling(self, nome:str):
        lista = []
        cursor.execute("SELECT * FROM linguagem WHERE nome = '{}'".format(nome))
        conn.commit()
        for linha in cursor.fetchall():
            equip = equip = {'id': linha[0], 'nome': linha[1], 'descricao': linha[2]}
            lista.append(equip)
        return lista

