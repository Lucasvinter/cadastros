class Equipes:
    def __init__(self, nome, linguagem, projeto, lider, integrante1, integrante2, integrante3, integrante4, id=None):
        self.id = id
        self.nome = nome
        self.linguagem = linguagem
        self.projeto = projeto
        self.lider = lider
        self.integrante1 = integrante1
        self.integrante2 = integrante2
        self.integrante3 = integrante3
        self.integrante4 = integrante4
        

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome    
        

    def get_projeto(self):
        return self.projeto


    def get_linguagem(self):
        return self.linguagem                


    def get_lider(self):
        return self.lider    
        

    def get_integrante1(self):
        return self.integrante1


    def get_integrante2(self):
        return self.integrante2


    def get_integrante3(self):
        return self.integrante3

        
    def get_integrante4(self):
        return self.integrante4
