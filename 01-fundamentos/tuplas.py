# Tupla e como uma lista porém imutável
# são colocados em parênteses 

produtos = ('Janela', 'porta', 'cama')

dados = ('Tiago', '07/12/23', '16:20')

#Outra forma de claração de tupla
nome, data, horario = dados

for dado in dados:
    print(dado)

for produto in produtos:
    print(produto)