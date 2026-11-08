from classes.Cliente import Cliente
import datetime
from classes.Extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(("DEPÓSITO", valor, datetime.datetime.today()))

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(("SAQUE", valor, datetime.datetime.today()))
            return True



    def transfere_valor(self,conta_destino, valor):
        if self.saldo < valor:
            return "Não Existe Saldo Suficiente"
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(("TRANSFERÊNCIA", valor, datetime.datetime.today(),))
            return "Transferência Realizada com sucesso."


    def gerar_extrato(self):
        print(f'Numero: {self.numero}')
        print(f'Saldo: R$:{self.saldo:10.2f}')
