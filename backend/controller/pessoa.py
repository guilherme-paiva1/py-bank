import backend.controller.conta
import backend.model.user

def cadastrar_usuario(nome, sexo, cpf, renda, senha):
    if not nome:
        return False
    if not sexo:
        return False
    if not cpf:
        return False
    if not renda:
        return False
    if not senha:
        return False

    dados = {
        "nome": nome,
        "cpf": cpf,
        "sexo": sexo,
        "renda": renda,
        "senha": senha
    }

    return backend.controller.conta.cadastrar_conta(dados)