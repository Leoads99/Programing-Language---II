'''
print('Endereco:', self.endereco) é uma forma
de dar exibir o endereço, você pode dar print através da classe Endereco
porém, por ser uma classe, resultará apenas em informações de memória da
classe printada, por isso a melhor forma de exibir o endereço nesse caso é
chamar através do método self (fazendo assim uma associação) o método
exibir_endereco(self)

Podemos utilizar dessa forma um método de outra classe dentro de outra
'''


class Endereco:
    def __init__(self, rua, numero, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = ""
        self.cep = cep

    def exibir_dados(self):
        print('Rua:', self.rua)
        print('Numero:', self.numero)
        print('Complemento:', self.complemento)
        print('CEP:', self.cep)


class Pessoa:
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def exibir_dados(self):
        print('Nome:', self.nome)
        print('Idade:', self.idade)
        print('Sexo:', self.sexo)
        self.endereco.exibir_dados()


end = Endereco('Rua Gato Cinzento', 809, 98290220)

pessoa1 = Pessoa('Leonardo', 21, 'M', end)

# pessoa1.exibir_dados()
print(pessoa1.endereco.rua)
