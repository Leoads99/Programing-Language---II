agenda = {'Maria': '99887766',
        'Pedro': '92345678',
        'Joaquim': '99887711'}

print(agenda['Joaquim'])      #printa o valor da key 'Joaquim' que é = '99887766'

agenda['Maria'] = '99991111'  #altera o valor da key 'Maria' 
#para inserir um novo item ao dicionário, deve-se atribuir um valor a uma chave inexistente 

#--- se a chave não existir, ela será criada 

#--- Dicionário não possui a função append

agenda = {}

agenda['Teresa'] = '65443322'  #cria novo item 

agenda['Maria'] = '99887766'   #cria novo item

agenda['Teresa'] = '99999999'  #altera o valor

agenda.pop('Teresa')           #remove item do dicionário 

agenda = {'Maria': '123456',
'João': '999900',
'Pedro': '999999'}

for x in agenda:
    print(x)                   #exibe todas as chaves 

for x in agenda:
    print(agenda[x])           #exibe todos os valores 
    
#Operador in pode ser utilizado para verificar se uma chave existe no dicionário 

if 'Maria' in  agenda:
    print ('A chave existe na agenda')
else:
    print('A chave não existe')
    
    
