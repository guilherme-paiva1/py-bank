import backend.controller.conta
import backend.controller.pessoa
import os

# Função responsável por introduzir o usuário ao programa
def dar_saudacao():
    print("Bem vindo ao banco Ary! Insira os dados solicitados para começar!")

# Função responsável por encerrar a execução do programa
def encerrar():
    print("Encerrar app")

# Função responsável por redirecionar o usuário para se cadastrar ou logar com conta já criada
def verificar_entrada():
    escolha = input("Você já tem cadastro? S/N").strip().lower() in ['sim', 'true', 's']
    if not escolha:
        backend.controller.pessoa.cadastrar_usuario()

    return backend.controller.pessoa.logar_usuario()

# Função responsável pela navegação entre funcionalidades
def navegar_menu(conta_bancaria):
    os.system('cls')
    escolha = int(input(f"""
    Seu saldo atual: R$ {conta_bancaria.saldo}
    Escolha uma opção:
    1. Depositar
    2. Transferir
    3. Sacar
    4. Pagar fatura (R$ {conta_bancaria.fatura})
    5. Encerrar
    """))

    # Sistema de direcionamento que envia o usuário para interação com a ação desejada
    # Depois, envia de volta para o menu principal, dependendo da decisão
    if escolha == 1:
        backend.controller.conta.depositar(conta_bancaria)
        navegar_menu(conta_bancaria)
    elif escolha == 2:
        backend.controller.conta.transferir(conta_bancaria)
        navegar_menu(conta_bancaria)
    elif escolha == 3:
        backend.controller.conta.sacar(conta_bancaria)
        navegar_menu(conta_bancaria)
    elif escolha == 4:
        backend.controller.conta.pagar_fatura(conta_bancaria)
        navegar_menu(conta_bancaria)
    elif escolha == 5:
        encerrar()
    else:
        print("Opção inválida!")
        navegar_menu(conta_bancaria)
    
# Ordem de execução da aplicação
def main():
    dar_saudacao()
    conta_bancaria = verificar_entrada()
    navegar_menu(conta_bancaria)
    
# Verificação que executa loop do programa
if __name__ == '__main__':
    main()