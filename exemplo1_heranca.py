class Veiculo:
    def __init__(self, marca, modelo, ano_fabricacao):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao

    def imprimir_informacoes(self):
        print("--------------------")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano fabricação:", self.ano_fabricacao)


# Carro herda da classe Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, quantidade_porta):
        super().__init__(marca, modelo, ano_fabricacao)     # chama o construtor da classe mãe
        self.quantidade_porta = quantidade_porta            # atributo especifico do Carro

    def imprimir_informacoes(self):
        super().imprimir_informacoes()                      # chama o método da classe mãe
        print('Portas: ', self.quantidade_porta)


# Moto herda da classe Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, partida_eletrica):
        super().__init__(marca, modelo, ano_fabricacao)     # chama o construtor da classe mãe
        self.partida_eletrica = partida_eletrica            # atributo especifico da Moto

    def imprimir_informacoes(self):
        super().imprimir_informacoes()                      # chama o método da classe mãe
        print('Partida Eletrica: ', self.partida_eletrica)


# cria objeto Carro
carro1 = Carro("Ford", "Ka", 2015, 4)
carro1.imprimir_informacoes()

# cria um objeto Moto
moto1 = Moto("Honda", "Biz", 2013, 'sim')
moto1.imprimir_informacoes()

# cria um objeto Veiculo
veic = Veiculo("marca", "modelo", 2010)
veic.imprimir_informacoes()