'''
Criar uma classe Pessoa.
- Atributos: nome, email, telefone.
- Métodos: Um método para exibir os dados desta pessoa.
'''


class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir(self):
        print('Nome: ', self.nome)
        print('Email: ', self.email)
        print('Telefone: ', self.telefone)


# cria um objeto
pessoa_1 = Pessoa('Pedro', 'pedro@email.com', 119999999)
print(pessoa_1.__dict__)                # __dict__ -> converte os atributos para um dicionario


# exemplo para cadastrar dois objetos em uma lista
lista = []
for i in range(2):
    nome = input('Nome do pessoa: ')
    email = input('Email da pessoa: ')
    telefone = int(input('Telefone da pessoa: '))
    pessoa = Pessoa(nome, email, telefone)
    lista.append(pessoa)

print(lista)

# exibe os dados de cada objeto da lista
for p in lista:
    p.exibir()