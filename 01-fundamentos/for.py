produtos = ['Relogio', 'Garrafa', 'controler-remoto', 'mesa']
qnt_producao = [100, 200, 300, 400, 500]

#Para garantir caso o tamanho da lista aumente
tamanho = len(produtos)

for i in range(tamanho):
    print('Produto: {} | Quandidade na produção: {}'. format(produtos[i], qnt_producao[i]))
    