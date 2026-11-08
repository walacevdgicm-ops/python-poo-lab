class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_clientes(self):
        print(f'Clientes do {self.nome}:')
        for cliente in self.clientes:
            print(f'{cliente.cpf:15s} {cliente.nome}')

    def listar_contas(self):
        print(f'Contas do {self.nome}:')
        for conta in self.contas:
            print(f'Numero: {conta.numero}  Saldo: R$ {conta.saldo:10.2f}')