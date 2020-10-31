# retorna a soma de dois números
def somar(a, b):
    return a + b

# calcula fatorial de um número inteiro positivo


def calcular_fatorial(n):
    f = 1
    for a in range(1, n+1):
        f *= a
    return f
