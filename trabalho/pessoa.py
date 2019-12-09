class Pessoa:
    def __init__(self, nome, sobrenome, cpf, id=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome

    def get_cpf(self):
        return self.cpf
