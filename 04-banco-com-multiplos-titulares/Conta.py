class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return "Não existe valor suficiente."
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor  # corrige: o valor precisa sair da conta de origem
            return "Transferência realizada com sucesso!"

    def gerar_extrato(self):
        print(f'Numero: {self.numero}\n Saldo: {self.saldo}')
