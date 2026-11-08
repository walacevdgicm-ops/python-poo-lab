from conta import Conta

c1 = Conta(11, 800)
c2 = Conta(22, 1000)
c3 = Conta(333, 500)

print(f'Até agora temos {Conta.get_total_contas()} conta(s) criadas')

c1.sacar(800)
c1.gerar_saldo()

c1.depositar(1000)
c1.gerar_saldo()
print(f'Muito Obrigado por ser Cliente do {Conta.nome_banco()}!')