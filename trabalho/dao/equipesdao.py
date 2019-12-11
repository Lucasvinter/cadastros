from model.equipes import Equipes
from dao.conexao import Conexao

class EquipesDao(Conexao):
     #--- Método para cadastrar uma equipe
    def cadastrar_equipe(self, equipes:Equipes):
        self.cursor.execute("INSERT INTO equipes VALUES (DEFAULT, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(equipes.get_nome(), equipes.get_linguagem(), equipes.get_projeto(), equipes.get_lider(), equipes.get_integrante1(), equipes.get_integrante2(), equipes.get_integrante3(), equipes.get_integrante4()))
        self.conn.commit()
    
    
    #--- Método para alterar uma equipe --- 
    def alterar_equipe(self, equipes:Equipes):
        self.cursor.execute("UPDATE equipes SET nome = '{}', linguagem = '{}', projeto = '{}', lider = '{}', integrante1 = '{}', integrante2 = '{}', integrante3 = '{}', integrante4 = '{}' WHERE id = {}".format(equipes.get_nome(), equipes.get_linguagem(), equipes.get_projeto(), equipes.get_lider(), equipes.get_integrante1(), equipes.get_integrante2(), equipes.get_integrante3(), equipes.get_integrante4(), equipes.get_id()))
        self.conn.commit()
    
    
    #--- Método para listar todos os equipes cadastradas
    def listar_equipe(self):   
        lista = []
        self.cursor.execute("SELECT * FROM equipes")
        self.conn.commit()
        for linha in self.cursor.fetchall():
            equip = {'id': linha[0], 'nome': linha[1], 'linguagem': linha[2], 'projeto': linha[3], 'lider': linha[4], 'integrante1': linha[5], 'integrante2': linha[6], 'integrante3': linha[7], 'integrante4': linha[8]}
            lista.append(equip)
        return lista
    
    
    #--- Metodo para excluir uma linha basenado-se no id recebido por parâmetro
    def deletar_equipe(self, id):
        self.cursor.execute("DELETE FROM equipes WHERE id = {}".format(id))
        self.conn.commit()
    
    #--- Metodo para filtrar uma equipes pelo 'Id' na lista de equipes cadastradas
    def filtro_id_equipe(self, id):
        lista = []
        self.cursor.execute("SELECT * FROM equipes WHERE id = {}".format(id))
        self.conn.commit()
        for linha in self.cursor.fetchall():
            equip = {'id': linha[0], 'nome': linha[1], 'linguagem': linha[2], 'projeto': linha[3], 'lider': linha[4], 'integrante1': linha[5], 'integrante2': linha[6], 'integrante3': linha[7], 'integrante4': linha[8]}
            lista.append(equip)
        return lista
    
    
    #--- Método para filtrar equipe por 'nome' na lista de equipes cadastradas
    def filtro_nome_equipe(self, nome):
        lista = []
        self.cursor.execute("SELECT * FROM equipes WHERE nome = '{}'".format(nome))
        self.conn.commit()
        for linha in self.cursor.fetchall():
            equip = {'id': linha[0], 'nome': linha[1], 'linguagem': linha[2], 'projeto': linha[3], 'lider': linha[4], 'integrante1': linha[5], 'integrante2': linha[6], 'integrante3': linha[7], 'integrante4': linha[8]}
            lista.append(equip)
        return lista

    def editar_equipe(self, id):
        lista = []
        self.cursor.execute("SELECT * FROM equipes WHERE id = {}".format(id))
        for linha in self.cursor.fetchall():
            person = {'id': linha[0], 'nome': linha[1], 'linguagem': linha[2], 'projeto': linha[3], 'lider': linha[4], 'integrante1': linha[5], 'integrante2': linha[6], 'integrante3': linha[7], 'integrante4': linha[8]}
            lista.append(person)
        return lista




        
