class Pessoa:
    def __init__(self, nome, sobrenome, cpf, data_nascimento, sexo, id=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome

    def get_cpf(self):
        return self.cpf

    def get_data_nascimento(self):
        return self.data_nascimento

    def get_sexo(self):
        return self.sexo
