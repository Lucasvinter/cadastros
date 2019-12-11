class Linguagem:
    def __init__(self, nome, descricao, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao


    def get_nome(self):
        return self.nome


    def get_descricao(self):
        return self.descricao

    def get_id(self):
        return self.id   