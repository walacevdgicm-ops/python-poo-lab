#Criando Uma Classe

class Conta:
    def __init__(self, num, titular, cpf_titular, saldo ):
        self.num = num
        self.titular = titular
        self.cpf_titular = cpf_titular
        self.saldo = saldo
    #Criando primeiro Metodo o metodo de sacar.
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque realizado com sucesso!\n Valor do Saque: {valor}")
    #Criando Metodo de depositar
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito realizado com sucesso.\n Valor Depositado {valor}")

    def gerar_comprovante(self):
        print(f" Numero da Conta: {self.num}\n Nome do Titular: {self.titular}\n CPF do Titular: {self.cpf_titular}\n Saldo Bancário: {self.saldo}")


    def transfere_valor(self, valor, conta_destino):
        if valor <= 0:
            raise ValueError("Transfira um valor maior do que 0.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para a transação. ")
        self.saldo -= valor
        conta_destino.saldo += valor
        print(f'Valor Transferido: {valor}')








if __name__ == "__main__":
    conta1 = Conta(1, "Walace", "111.111.111-11", 1000)
    conta2 = Conta(2, "Maria", "222.222.222-22", 500)
    conta1.sacar(200)
    conta1.depositar(50)
    conta1.transfere_valor(300, conta2)
    conta1.gerar_comprovante()
    conta2.gerar_comprovante()
