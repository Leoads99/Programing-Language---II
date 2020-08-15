salario = float(input('Digite seu salário:'))

if salario > 2.000:
    salario7 = salario + 7/100*salario
    print ('O salário com o reajuste de 7% será:', salario7)
else:
    salario15 = salario + 15/100*salario
    print('O salário com o reajuste de 15% será:', salario15)