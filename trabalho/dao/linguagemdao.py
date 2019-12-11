from model.linguagem import Linguagem
from dao.conexao import Conexao

class LinguagemDao(Conexao):
     #--- Método para cadastrar uma linguagem
    def cadastrar_ling(self, linguagem:Linguagem):
        self.cursor.execute("INSERT INTO linguagem VALUES (DEFAULT, '{}', '{}')".format(linguagem.get_nome(), linguagem.get_descricao()))
        self.conn.commit()
    
    
    #--- Método para alterar uma linguagem --- 
    def alterar_ling(self, linguagem:Linguagem):
        self.cursor.execute("UPDATE linguagem SET nome = '{}', descricao = '{}' WHERE id = {}".format(linguagem.get_nome(), linguagem.get_descricao(), linguagem.get_id()))
        self.conn.commit()
    
    
    #--- Método para listar todos os linguagem cadastradas
    def listar_ling(self):   
        lista = []
        self.cursor.execute("SELECT * FROM linguagem")
        self.conn.commit()
        for linha in self.cursor.fetchall():
            equip = {'id': linha[0], 'nome': linha[1], 'descricao': linha[2]}
            lista.append(equip)
        return lista
    
    
    #--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
    def deletar_ling(self, id):
        self.cursor.execute("DELETE FROM linguagem WHERE id = {}".format(id))
        self.conn.commit()
    
    #--- Metodo para filtrar uma linguagem pelo 'Id' na lista de linguagem cadastradas
    def filtro_id_ling(self, id):
        lista = []
        self.cursor.execute("SELECT * FROM linguagem WHERE id = {}".format(id))
        self.conn.commit()
        for linha in self.cursor.fetchall():
            equip = {'id': linha[0], 'nome': linha[1], 'descricao': linha[2]}
            lista.append(equip)
        return lista
    
    
    #--- Método para filtrar funcionario por 'nome' na lista de linguagem cadastradas
    def filtro_nome_ling(self, nome):
        lista = []
        self.cursor.execute("SELECT * FROM linguagem WHERE nome = '{}'".format(nome))
        self.conn.commit()
        for linha in self.cursor.fetchall():
            equip = {'id': linha[0], 'nome': linha[1], 'descricao': linha[2]}
            lista.append(equip)
        return lista

    def editar_ling(self, id):
        lista = []    
        self.cursor.execute("SELECT * FROM linguagem WHERE id = {}".format(id))
        for linha in self.cursor.fetchall():
            person = {'id': linha[0], 'nome': linha[1], 'descricao': linha[2]}
            lista.append(person)
        return lista   