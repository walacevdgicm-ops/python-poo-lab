# Criar um programa de cadastro em uma "Plataforma fictícia" 1°Passo: Receber as informações necessárias

print('Seja Bem vindo à nossa plataforma de Streaming, para dar início à nossa Jornada vamos fazer o seu Cadastro.')
print('Precisaremos de algumas informações sobre você.')

#Aqui você recebe o nome completo do usuário e retorna a ele às boas vindas

nome = str(input("Digite o seu nome completo: "))
print('Olá {}! Muito prazer em recebêlo em nossa plataforma, vamos seguir com nosso cadastro.'.format(nome))

# Agora diremos para o usuário que pediremos seu cpf, leia o CPF do usuário e prossiga com o cadastro sempre com feefback

print('{}, Para darmos início vou pedir agora o seu CPF'.format(nome))

cpf = str(input('Digite o seu CPF: '))
print('Ok, agora precisamos saber qual a sua data de nascimento')
from datetime import datetime

while True:
    nascimento = input('Digite sua data de nascimento (dd/mm/aaaa): ')
    try:
        data_nascimento = datetime.strptime(nascimento, '%d/%m/%Y')
        break
    except ValueError:
        print('Data inválida, use o formato dd/mm/aaaa.')

idade = (datetime.now() - data_nascimento).days // 365
if idade < 18:
    print('Como você é menor de idade, sua conta terá o perfil Kids com controle dos pais.')

email = input('Agora, qual é o seu e-mail? ')

print('\nEscolha o seu plano:')
planos = {'1': ('Básico', 19.90), '2': ('Padrão', 39.90), '3': ('Premium', 59.90)}
for codigo, (nome_plano, preco) in planos.items():
    print(f'  [{codigo}] {nome_plano} - R$ {preco:.2f}/mês')

opcao = input('Digite o número do plano: ')
while opcao not in planos:
    opcao = input('Opção inválida. Digite 1, 2 ou 3: ')

plano, preco = planos[opcao]

print('\n===== RESUMO DO CADASTRO =====')
print(f'Nome: {nome}')
print(f'CPF: {cpf}')
print(f'Idade: {idade} anos')
print(f'E-mail: {email}')
print(f'Plano: {plano} (R$ {preco:.2f}/mês)')
print(f'\nTudo pronto, {nome}! Bom streaming! 🎬')
