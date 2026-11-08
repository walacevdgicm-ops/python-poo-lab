from Cliente import Cliente
from Conta import Conta

# testando o codigo

cliente1 = Cliente(88838, "João", "Rua x")
cliente2 = Cliente(2222444, "Maria", "Rua Y")
cliente3 = Cliente(2222222, "Estefan","Rua ABC")
cliente4 = Cliente(3333333, "Damon","Rua Mystic")

conta1 = Conta([cliente1, cliente2], 111, 0)
conta2 = Conta([cliente3, cliente4], 222, 300)


conta1.depositar(500)
conta1.sacar(300)




conta2.depositar(10000)
conta2.sacar(700)





conta2.transfere_valor(conta1, 1000)
conta1.gerar_extrato()
conta2.gerar_extrato()
