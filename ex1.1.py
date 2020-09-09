"""
Ex 01 - 
Preencha uma lista com 10 números digitados pelo usuário e exiba: 
a - O maior número da lista
b - O menor número da lista
c - a média dos números contidos na lista
d - todos os números menores do que a média calculada no item anterior 


cont = 0

lista = []


while cont <10:
    numeros = int(input('Digite dez números:'))
    lista.append(numeros)
    cont = cont+1
else:
    media = sum(lista)/ len(lista)
    print ('o maior número é',(max(lista)))
    print ('o menor número é',(min(lista)))
    print ('A média dos números é', media)
    print (min(lista))
    
    print ('Números menores que a média')
    for a in lista:
        if a < media:
            print(i)
            
            
Ex 02 - 

Preencha uma lista com 20 números 
sorteados aleatóriamente 
(utilize a função randint do módulo random para sortear os números).


from random import randint      

cont = 0
lista = []

while cont<20: 
    num = randint(1,500)
    lista.append(num)
    cont = cont+1
else:
    print ('A lista de números gerados é:', lista)

Exercício 03

Preencha uma lista com 10 números sorteados aleatóriamente. A partir desta lista, gere uma lista com os números pares e outra lista com os números ímpares. 

Exemplo: 
Suponha que a lista com os números sorteados seja: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8]. 
Para esta lista, o programa deve gerar as seguintes listas:
[4, 8, 8]
[1, 7, 9, 5, 3, 7, 9]


from random import randint      

lista = []
for a in range(20): 
    num = randint(0,100)
    lista.append(num)

pares = []
impares = []

for a in lista:
    if a % 2 == 0:
        pares.append(a)
    if a % 2 == 1:
        impares.append(a)
print (f'A lista de números pares é {pares}')
print (f'A lista de números ímpares é {impares}')

Exercício 04

Faça um programa que simule um lançamento de dados. O programa deve sortear 10 números aleátorios (de 1 a 6) e armazenar esses números em uma lista. 
Na sequência, informe quantas vezes cada número foi sorteado.

Exemplo: 
Suponha que a lista com os números sorteados seja: [3, 1, 5, 3, 5, 4, 5, 5, 3, 1]. 
Para esta lista, o programa deve exibir:
Número 1 foi sorteado 2 vezes
Número 2 foi sorteado 0 vezes
Número 3 foi sorteado 3 vezes
Número 4 foi sorteado 1 vezes
Número 5 foi sorteado 4 vezes
Número 6 foi sorteado 0 vezes

"""
from random import randint 

lista_dado = []
cont = 0
while cont<10:
    sorteio = randint(1,10)
    lista_dado.append(sorteio)
    cont = cont+1
for a in lista_dado:
    print(f'Número {a} foi sorteado {lista_dado.count(cont)} vezes')
print (lista_dado)