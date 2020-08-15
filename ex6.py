def divisores (n):
    soma = 0
    for i in range (1, n+1):
        if n % i == 0:
            soma += i
    return soma

num = int(input('Informe um número: '))
print("Soma dos divisores: " ,divisores(num))