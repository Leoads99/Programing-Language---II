class AnimalTerrestre:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print('Animal Terrestre está Andando')

    def comer(self):
        print('Animal Terrestre está Comendo')


class AnimalAquatico:
    def __init__(self, nome):
        self.nome = nome
        self.teste = ''

    def nadar(self):
        print('Animal Aquatico está Nadando')

    def comer(self):
        print('Animal Aquatico está Comendo')


# Herança Múltipla (ocorre quando uma classe herda de duas ou mais classes)
# a primeira classe herdada terá prioridade
class Anfibio(AnimalTerrestre, AnimalAquatico):
    def __init__(self, nome):
        AnimalTerrestre.__init__(self, nome)
        AnimalAquatico.__init__(self, nome)

    def comer(self):
        AnimalAquatico.comer(self)
        AnimalTerrestre.comer(self)


animal = Anfibio('Nome do animal')
animal.comer()
