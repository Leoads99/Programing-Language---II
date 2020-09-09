# EXEMPLO 1:
# Criar dicionario para armazenar um cadastro de pessoas (CPF e NOME)
cadastro = {123456: "Paulo", 
            888888: "Ana", 
            555555: "Pedro"}
print(cadastro)
print(cadastro[123456])

# Adicionar os dados de uma pessoa no dicionario
cadastro[333333] = "Maria"
print(cadastro)

# Alterar o Nome de uma pessoa
cadastro[123456] = "Paulo Vieira"
print(cadastro)

# Excluir os dados de uma pessoa
cadastro.pop(123456)
print(cadastro)

# Verificar se chave existe no dicionário
if 123455 in cadastro:
    cadastro.pop(123455)
else:
    print("Chave inexistente")
    
# Percorrer as chaves do dicionario com o FOR
for a in cadastro:
    print(a, cadastro[a])

# preencher dicionário com dados informados pelo usuário
'''
cadastro = {}
for a in range(3):
    cpf = int(input("CPF: "))
    nome = input("Nome: ")
    cadastro[cpf] = nome
print(cadastro)

cpf = int(input("CPF: "))
nome = input("Nome: ")
cadastro[cpf] = nome
'''    

# EXEMPLO 2:
# Dicionario para armazenar o nome de um aluno e uma lista com 3 notas
alunos = {'Paulo': [7,8,10], 'Ana': [6,7,8], 'Pedro': [8, 5, 7]}
print(alunos)

# Exibir notas de um aluno
print(alunos['Paulo'])

# alterar uma nota especifica
alunos['Paulo'][0] = 7.5
print(alunos)

# Inserir uma nova nota para um aluno 
alunos['Paulo'].append(6.5)
print(alunos)

