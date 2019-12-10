from conexao import conn, cursor

class Funcao:
    #--- Método para cadastrar um funcionario
    def cadastrar_func(self, nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria):
        cursor.execute("INSERT INTO funcionarios VALUES (DEFAULT, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria))
        conn.commit()
    
    
    #--- Método para alterar um funcionario --- 
    def alterar_func(self, nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria, id:int):
        cursor.execute("UPDATE funcionarios SET nome = '{}', sobrenome = '{}', cpf = '{}', data_nascimento = '{}', sexo = '{}', cargo = '{}', salario = '{}', carga_horaria = '{}' WHERE id = {}".format(nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria, id))
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
    def cadastrar_equipe(self, nome, linguagem, lider, projeto, integrante1, integrante2, integrante3, integrante4):
        cursor.execute("INSERT INTO equipes VALUES (DEFAULT, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(nome, linguagem, lider, projeto, integrante1, integrante2, integrante3, integrante4))
        conn.commit()
    
    
    #--- Método para alterar um funcionario --- 
    def alterar_equipe(self, nome, linguagem, lider, projeto, integrante1, integrante2, integrante3, integrante4, id):
        cursor.execute("UPDATE equipes SET nome = '{}', linguagem = '{}', projeto = '{}', lider = '{}', integrante1 = '{}', integrante2 = '{}', integrante3 = '{}', integrante4 = '{}' WHERE id = {}".format(nome, linguagem, lider, projeto, integrante1, integrante2, integrante3, integrante4, id))
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
    def cadastrar_ling(self, nome, descricao):
        cursor.execute("INSERT INTO linguagem VALUES (DEFAULT, '{}', '{}')".format(nome, descricao))
        conn.commit()
    
    
    #--- Método para alterar um funcionario --- 
    def alterar_ling(self, nome, descricao, id):
        cursor.execute("UPDATE linguagem SET nome = '{}', descricao = '{}' WHERE id = {}".format(nome, descricao, id))
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

