import database.database_ops

def entrar(cpf, senha):
    contas = database.database_ops.carregar_dados() 

    # Procura pelas informações fornecidas nas contas cadastradas
    for conta in contas:
        cpf_atual = conta["dono"]["cpf"]
        senha_atual = conta["dono"]["senha"]

        print("CPF atual da iteração: ", cpf_atual)
        print("Senha atual da iteração: ", senha_atual)
        # Verifica se o CPF e senha informados são iguais às informações atuais da iteração
        if cpf == cpf_atual and senha_atual == senha:
            return conta
        
    return False

def cadastrar(conta):
    return database.database_ops.salvar_dados(conta)

# Função responsável por procurar uma conta pelo CPF informado
def buscar_cpf(cpf):
    contas = database.database_ops.carregar_dados()
    # Procura com uma estrutura de repetição
    for conta in contas:
        cpf_atual = conta["dono"]["cpf"]

        # Verifica se o CPF informado é igual ao CPF atual na iteração
        if cpf == cpf_atual:
            return conta
    
    # Caso não encontre após o fim da iteração, informa que o CPF não foi encontrado,
    # pois o mesmo não existe na base de dados
    print("CPF não encontrado!")

# Função responsável por atualizar o saldo de acordo com o CPF informado
# Espera pelo CPF do dono da conta e pelo novo saldo a ser gravado 
def atualizar_saldo(cpf, novo_saldo):
    contas = database.database_ops.carregar_dados()
    
    # Procura com uma estrutura de repetição
    for conta in contas:
        cpf_atual = conta["dono"]["cpf"]
        # Verifica se o CPF informado é igual ao CPF atual na iteração
        if cpf_atual == cpf:  
            # Se sim, atualiza o saldo de acordo
            conta["saldo"] = novo_saldo
            break

    database.database_ops.atualizar_dados(contas)
    print("Saldo atualizado com sucesso!")

# Atualiza o crédito e a fatura de acordo com os valores informados
# Aguarda o CPF da conta a ser atualizada, o novo crédito a ser gravado e o valor usado na operação
def atualizar_credito(cpf, novo_credito, valor_usado):
    contas = database.database_ops.carregar_dados()
    
    for conta in contas:
        cpf_atual = conta["dono"]["cpf"]
        if cpf_atual == cpf:  
            conta["credito_disponivel"] = novo_credito
            conta["fatura"] = conta["fatura"] + valor_usado
            
    database.database_ops.atualizar_dados(contas)
    print("Credito atualizado com sucesso!")

def atualizar_fatura(cpf, fatura):
    contas = database.database_ops.carregar_dados()
    
    for conta in contas:
        cpf_atual = conta["dono"]["cpf"]
        if cpf_atual == cpf:  
            conta["credito_disponivel"] = conta["credito_disponivel"] + fatura
            conta["fatura"] = 0
            break

    database.database_ops.atualizar_dados(contas)
    print("Credito atualizado com sucesso!")