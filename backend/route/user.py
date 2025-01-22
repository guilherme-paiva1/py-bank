from fastapi import APIRouter
from backend.controller import conta
from backend.controller import pessoa
from pydantic import BaseModel

router = APIRouter()

class DadosLogin(BaseModel):
    cpf: str
    senha: str

class DadosCadastro(BaseModel):
    nome: str
    sexo: str
    cpf: str
    renda: int
    senha: str

@router.post("/entrar")
def entrar(dados: DadosLogin):
    resposta = conta.entrar(dados.cpf, dados.senha) 
    return resposta

@router.post("/cadastrar")
def cadastrar(dados: DadosCadastro):
    resposta = pessoa.cadastrar_usuario(dados.nome, dados.sexo, dados.cpf, dados.renda, dados.senha)
    return resposta