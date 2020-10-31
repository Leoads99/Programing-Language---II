'''
* Encapsulamento diz respeito à proteção
dos atributos ou métodos de uma classe

* Consiste em separar aspectos externos
de um objeto dos detalhes internos de
implementação

* Evita que dados específicos de uma aplicação
possa ser acessado diretamente

* Em Python, ao aplicar o conceito
de Encapsulamento, os atributos e
métodos podem ser:

- Públicos (os que podemos acessar fora da classe)
- ou
- Privados (os que podemos acessar somente dentro da classe)

* Atributos ou métodos com nomes
iniciados por dois sublinhados
são privados e todas as
outras formas são públicas

* Aplicando o conceito de encapsulamento, os
atributos e métodos privados de uma classe
ficam ocultos do restante da aplicação

* Para permitir o acesso é necessário criar
métodos públicos que acessem os atributos privados

* Para isso a prática mais comum é criar dois métodos:

- um que retorna o valor do atributo (get)

- e outro que altera o valor do atributo (set)

* A vantagem no uso dos métodos get e set
é que estes métodos podem ser usados para
validação de acesso
'''

'PRIMEIRO EXEMPLO'


class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        # Atributos Públicos
        self.nome = nome
        self.idade = idade
        # Atributos Privados
        self.__cpf = cpf
        self.__rg = rg

    def get_cpf(self):
        # Métodos get
        # retornam valor do atributo
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def set_cpf(self, cpf):
        # Métodos set
        # alteram valor do atributo
        if len(str(cpf)) == 11:
            self.__cpf = cpf
        else:
            print("Valor inválido")

    def set_rg(self, rg):
        self.__rg = rg

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("CPF:", self.__cpf)
        print("RG:", self.__rg)


pessoa1 = Pessoa("Leo", 20, 47553203800, 376256035)
pessoa1.nome = "Leonardo Andrade de Souza"
pessoa1.idade = 21
pessoa1.set_cpf(47553203807)
# para exibir o cpf através do atributo get
print("CPF:", pessoa1.get_cpf())
pessoa1.exibir_dados()
# print(pessoa1.nome)
# print(pessoa1.__cpf)        # ERRO
