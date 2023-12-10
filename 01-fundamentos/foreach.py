produtos = ['Televisão', 'Rádio', 'Celular', 'Geladeira']

# for produto in produtos:
#     print('Prduto: {}'.format(produto))
    

# Lista de vendas dos vendedores
vendedores = ['Ana', 'João', 'Miguel','Antônio']
vendas = [10, 5, 17, 50]
meta = 50

for i in range(4):
    if vendas[i] >= meta:
        print('Vendedor: {} vendeu {} produtos, atingiu a meta'.format(vendedores[i], vendas[i]))
    else:
        print('')
        print('Vendedor: {} não atingiu a meta!'.format(vendedores[i])) 
        print('')   
    