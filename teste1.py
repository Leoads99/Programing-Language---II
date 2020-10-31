"""
* assert (verificação) é como se fosse um if
porém é usado para teste

* Podemos usar vários asserts para indicarmos
diversas verificações de erros

* E também podemos colocar uma mensagem
de acordo com o contexto do erro
"""

from modulo1 import somar, calcular_fatorial


def teste1():
    try:
        resultado = somar(10, 20)
        assert resultado > 0, 'Resultado não é positivo'
        assert resultado % 2 == 0, 'Resultado não é par'
        assert resultado == 30, 'Resultado não é 30'
        print('CORRETO')
    except AssertionError as x:
        print('ERRO:', resultado, x)


def teste2():
    try:
        resultado = somar(-50, -50)
        assert resultado == -100
        print('CORRETO')
    except AssertionError:
        print('ERRO')


def teste_fatorial():
    try:
        resultado = calcular_fatorial(5)
        assert resultado == 120
        print('Fatorial CORRETO')
    except AssertionError:
        print('ERRO no fatorial')


teste1()
teste2()
teste_fatorial()
