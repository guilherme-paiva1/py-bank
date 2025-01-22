# Classe auxiliar para criação de objetos Conta:
# Aqui são armazenadas as informações pessoais do dono de uma conta.
# Nome, sexo e CPF esperam uma string
# Renda espera um integer
class Pessoa():
    def __init__(self, nome, sexo, cpf, renda):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.renda = renda