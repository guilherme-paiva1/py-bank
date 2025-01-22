import json

# Seleciona o arquivo usado como Banco de Dados
arquivo_db = "database/database.json"

# Carrega todos os dados do arquivo do Banco de Dados e os retorna
def carregar_dados():
    try:
        with open(arquivo_db, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        # Retorna uma lista vazia se o arquivo não existir
        return []

# Salva novos dados no arquivo de Banco de Dados
# A função espera por um dicionário Python
def salvar_dados(dados):
    # Carrega os dados existentes do arquivo
    dados_existentes = carregar_dados()

    # Adiciona os novos dados à lista de dados extraída do arquivo
    dados_existentes.append(dados)
    
    # Salva todos os dados de volta no arquivo
    with open(arquivo_db, "w") as arquivo:
        json.dump(dados_existentes, arquivo, indent=4)
        
    return True

# Função responsável por atualizar informações
# Essa função soluciona a não quebra da formatação do arquivo JSON
# A função espera por um dicionário Python
def atualizar_dados(dados):
    with open(arquivo_db, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)