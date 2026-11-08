from classes.Banco import Banco
from classes.Cliente import Cliente
from classes.Conta import Conta

banco = Banco("Meu Banco")

cliente1 = Cliente("111.111.111-11", "Walace", "Rua A, 10")
cliente2 = Cliente("222.222.222-22", "Maria", "Rua B, 20")
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

conta1 = Conta(cliente1, 555, 0)
conta2 = Conta(cliente2, 556, 0)
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

conta1.depositar(500)

banco.listar_clientes()
banco.listar_contas()
# Conta especial com limite (cheque especial)
from classes.ContaEspecial import ContaEspecial

conta3 = ContaEspecial(cliente1, 557, 100, limite=500)
banco.adicionar_conta(conta3)
conta3.sacar(400)        # usa R$ 300 do limite
conta3.sacar(1000)       # recusado: passa do limite
conta3.gerar_extrato()

# Transferência entre contas e extrato detalhado
print(conta1.transfere_valor(conta2, 200))
conta1.extrato.gerar_extrato1(conta1.numero)
banco.listar_contas()
