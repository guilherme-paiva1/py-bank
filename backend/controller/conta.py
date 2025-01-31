from backend.packages.Conta import Conta
from backend.packages.Pessoa import Pessoa
from backend.model import user

def entrar(cpf, senha):
    if not cpf:
        return False
    if not senha:
        return False

    conta = user.entrar(cpf, senha)
    return conta

def cadastrar_conta(dados):
    renda = dados["renda"]
    
    if renda >= 0 and renda <= 500:
        credito = 1000
    elif renda > 500 and renda <= 1000:
        credito = 2000
    elif renda > 1000 and renda <= 2000:
        credito = 5000
    
    conta_bancaria = {
        "saldo": 0,
        "credito": credito,
        "fatura": 0,
        "dono": dados
    }

    status = user.cadastrar(conta_bancaria)
    
    return status