products = {}

for a in range(5):
    name_product = str(input('Digite o nome do produto: '))
    price = float(input('Digite o preço do produto: '))
    products[name_product]=price

print(products)

print ('Produtos com valor superior a 50.00:')
for a in products:
    if products[a] > 50:
        print(a)
    
"""
alunos = {}

notas =[]

for a in range(0,3):
    nota = int(input('Digite 3 notas: '))
    notas.append(nota)
nome = str(input('Digite o seu nome: '))
print(notas)
"""