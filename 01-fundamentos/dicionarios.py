#Dicionário

dicionario_pessoa = {
    'nome':'Tiago',
    'idade': 36,
    'cidade': 'Porto Alegre'
    }

# Outra maneira de cirar um dicionário 
dicionario_pessoa2 = dict(nome = 'Lucia', idade = '35', cidade = 'Salvador')

print(dicionario_pessoa.keys())
print(dicionario_pessoa2.items())

for item in dicionario_pessoa.items():
    print(item[1])    
