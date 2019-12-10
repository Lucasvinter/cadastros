from model.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, data_nascimento, sexo, cargo, salario, carga_horaria, id=None):
        super().__init__(nome, sobrenome, cpf, data_nascimento, sexo, id)
        self.salario = salario
        self.cargo = cargo
        self.carga_horaria = carga_horaria

    def get_salario(self):
        return self.salario

    def get_cargo(self):
        return self.cargo

    def get_carga_horaria(self):
        return self.carga_horaria
