from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, salario, cargo, carga_horaria=None):
        self.salario = salario
        self.cargo = cargo
        self.carga_horaria = carga_horaria

    def get_salario(self):
        return self.salario

    def get_cargo(self):
        return self.cargo

    def get_carga_horaria(self):
        return self.carga_horaria
