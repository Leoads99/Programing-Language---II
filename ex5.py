def divisores (n):
    for i in range (1, n+1):
        if n % i == 0:
            print (i)

num = int(input('Informe um número: '))
divisores(num)