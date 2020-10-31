'''
Classe Cachorro
- Atributos: nome, idade
- Métodos: andar, comer, latir
'''


class Cachorro:
    # atributos
    def __init__(self, nome, idade):        # construtor
        self.nome = nome
        self.idade = idade

    # metodos
    def andar(self, distancia):
        print('O cachorro andou ' + str(distancia) + ' metros')

    def comer(self):
        print('O cachorro de nome ' + self.nome + ' comeu')

    def latir(self):
        print('Au Au..,')


dog = Cachorro('Rex', 4)
dog.nome = 'Rex'
print('O cachorro de nome ' + dog.nome +
    ' possui a idade de ' + str(dog.idade) + ' anos')
dog.andar(2)
dog.latir()
dog.comer()

meu_cachorro = Cachorro('Snoopy', 2)
meu_cachorro.nome = 'Snoopy'
print('O cachorro de nome ' + meu_cachorro.nome +
    ' possui a idade de ' + str(meu_cachorro.idade) + ' anos')
meu_cachorro.andar(5)
meu_cachorro.latir()
meu_cachorro.comer()
meu_cachorro = Cachorro('Snoopy', 2) 