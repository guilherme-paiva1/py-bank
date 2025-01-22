# Pacote de operações com o Banco de Dados NoSQL
import backend.model.user
# Pacote utilizado para prover ao usuário algum tempo para ler as informações
import time

# Classe que armazena informações da conta de um usuário
class Conta():
    # O atributo dono se refere a um objeto de classe "Pessoa"
    # Saldo, credito e fatura são números manipuláveis por matemática
    def __init__(self, dono, saldo, credito, fatura):
        self.dono = dono
        self.saldo = saldo
        self.credito = credito
        self.fatura = fatura
    
    # Função responsável por realizar transferências entre contas
    # A função transferir recebe:
    # 1. O valor da transferência, 2. Objeto de classe Conta que demarca o destino da transferência
    def transferir(self, valor, destino):
        # Verificação para uso exclusivo do saldo
        if self.saldo > valor:
            print("Tudo certo com a operação!")
        # Verificação para uso do crédito como complemento
        elif (self.saldo + self.credito) > valor:
            print(f"""
                Valor da operação: R$ {valor}
                Seu saldo atualmente: R$ {self.saldo}
                Seu crédito atualmente: R$ {self.credito}
                Crédito que será usado: R$ {valor - self.saldo}""")
            escolha = input("Você não tem o valor necessário para essa operação! Deseja completar o valor via crédito? S/N").strip().lower() in ['sim', 'true', 's']
            # Verificação pelo desejo do usuário de utilizar seu crédito
            if escolha:
                credito_a_usar = valor - self.saldo
                self.sacar(valor)
                self.usar_credito(credito_a_usar)
                print("Seu crédito agora: ", self.credito)
                print("Sua fatura agora: ", self.fatura)
            # Caso não seja do interesse do usuário, cancela o uso do crédito e a operação de transferência
            else:
                print("Operação cancelada!")
            
            time.sleep(2)
            return
        # Caso o usuário não tenha saldo nem crédito para finalizar a transferência, o informa e volta para o menu
        else:
            print("Você não tem saldo, nem crédito suficientes para essa operação!")
            time.sleep(2)
            return
        self.saldo = self.saldo - valor
        backend.model.user.atualizar_saldo(self.dono.cpf, self.saldo)
        
        destino.depositar(valor)
        backend.model.user.atualizar_saldo(destino.dono.cpf, destino.saldo)
        print("Transferência realizada com sucesso!")
    
    # Função responsável por adicionar dinheiro na conta do usuário
    # Espera o valor a ser depositado na conta em integer
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        backend.model.user.atualizar_saldo(self.dono.cpf, self.saldo)
        print("Depósito realizado com sucesso!")
    
    # Função responsável por remover dinheiro da conta do usuário
    # Espera o valor a ser sacado da conta em integer
    def sacar(self, valor):
        # Verifica se o usuário tem dinheiro suficiente para sacar
        if valor > self.saldo:
            print("Você não tem saldo suficiente para sacar essa quantidade!") 
            time.sleep(2)
            return
        self.saldo = self.saldo - valor
        backend.model.user.atualizar_saldo(self.dono.cpf, self.saldo)
        print("Saque realizado com sucesso!")
    
    # Função chamada quando o usuário invoca a opção de utilizar o crédito para completar uma ação
    # Espera o valor a ser utilizado do crédito do usuário
    def usar_credito(self, valor):
        # Verifica se o usuário tem crédito suficiente para operação
        if valor > self.credito:
            print("Você não tem crédito suficiente para essa ação!")
            time.sleep(2)
            return
        self.credito = self.credito - valor
        backend.model.user.atualizar_credito(self.dono.cpf, self.credito, valor)
    
    # Função para pagar fatura
    # Restaura o crédito e a fatura para os estados originais, descontando do saldo do usuário
    def pagar_fatura(self):
        self.saldo = self.saldo - self.fatura
        self.credito = self.credito + self.fatura
        backend.model.user.atualizar_fatura(self.dono.cpf, self.fatura)

        self.fatura = 0

        
        