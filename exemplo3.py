'''
Criar uma classe Aluno
- Atributos: ra, nome, email, lista de notas.
- Métodos: inserir_nota, calcular_media
'''


class Aluno:
    def __init__(self, ra, nome, email):
        self.ra = ra
        self.nome = nome
        self.email = email
        self.lista_notas = []

    def inserir_nota(self, nota):
        self.lista_notas.append(nota)

    def calcular_media(self):
        media = sum(self.lista_notas) / len(self.lista_notas)
        return media


aluno_1 = Aluno(11111111, 'Joao', 'joao@email.com')
aluno_2 = Aluno(22222222, 'Pedro', 'pedro@email.com')

aluno_1.inserir_nota(8)
aluno_1.inserir_nota(7.5)
aluno_1.inserir_nota(8.25)
media = aluno_1.calcular_media()
print(f'Média: {media:.2f}')

aluno_2.inserir_nota(6)
aluno_2.inserir_nota(7)
aluno_2.inserir_nota(8)
print(f'Média: {aluno_2.calcular_media():.2f}')