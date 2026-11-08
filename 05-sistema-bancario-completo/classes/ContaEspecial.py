from classes.Conta import Conta
import datetime


class ContaEspecial(Conta):
    """Conta com limite (cheque especial): permite sacar além do saldo até o limite."""

    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f'Não existe saldo suficiente na conta número {self.numero}')
            return False
        self.saldo -= valor
        self.extrato.transacoes.append(("SAQUE ESPECIAL", valor, datetime.datetime.today()))
        if self.saldo < 0:
            print(f'Atenção: conta {self.numero} usando R$ {abs(self.saldo):.2f} do limite.')
        return True

    def gerar_extrato(self):
        super().gerar_extrato()
        print(f'Limite disponível: R$ {self.limite + min(self.saldo, 0):10.2f}')
