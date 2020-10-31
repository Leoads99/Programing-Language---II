'''
try:
    Operação a ser realizada
except Nome_Tipo_de_exceção: # Podem
    falha ocorrida
except Nome_Tipo_de_exceção: # haver várias
    falha ocorrida
except Nome_Tipo_de_exceção: # exeções
    falha ocorrida
else:
    se não houver problema
finally:
    finalmente, volte sempre
'''

# EXEMPLO DE USO DO TRY E EXCEPT
# USO DE EXCEÇÕES


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
