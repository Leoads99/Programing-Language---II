# EXEMPLO 1:
# Criar dicionário para armazenar um cadastro de pessoas (CPF e NOME)
cadastro = {123456: 'Paulo',
            888888: 'Ana',
            555555: 'Pedro'}
print(cadastro)
print(cadastro[123456])

# Adicionar os dados de uma pessoa no dicionário
cadastro[123456] = 'Paulo Vieira'
print(cadastro)

# Excluir os dados de uma pessoa
cadastro.pop(123456)
print(cadastro)

# Verificar se chave existe no dicionário
if 123455 in cadastro:
    cadastro.pop(123455)
else:
    print('Chave inexistente')

cadastro = {}
for x in range(3):
    cpf = int(input("CPF: "))
    nome = input("Nome: ")
    cadastro[cpf] = nome
print(cadastro)
