# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1:
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:


'''
Escreva uma função com o nome quantidade, que recebe como argumentos de
entrada uma tupla e um item e retorna quantas vezes esse item aparece na
tupla.
'''


def quantidade(tupla, item):
    return tupla.count(item)


'''
Escreva uma função chamada excluir que recebe como argumentos de entrada uma
lista e um item e retorna a lista sem o item informado.
'''


def excluir(lista, item):
    while item in lista:
        lista.remove(item)
    return lista


'''
Escreva uma função chamada posicoes_lista que recebe como argumentos de entrada
uma lista e um item, e retorna uma lista contendo todas os índices em que o
item aparece na lista.
'''

def posicoes_lista(lista, item):
    posicoes_item = []
    posicao_item = 0
    for x in lista:
        if x == item:
            posicoes_item.append(posicao_item)
            posicao_item += 1
    return posicoes_item


'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
3 notas. Escreva uma função chamada aprovados que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos aprovados
(um aluno é aprovado quando a média das suas notas é maior ou igual a 6).
'''
def aprovados(dicionario):
    for x in alunos:
        media = alunos[x]
        media = sum(media)/len(media)
        if media >= 6.0:
            alunos_aprovados.append(x)
    return (alunos_aprovados)


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
3 notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
'''
def incluir_nota(alunos, nome, nota):
    pass

