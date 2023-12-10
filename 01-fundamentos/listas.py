# lista no python são dinâmicas aceitam qualquer tipo de dado
# append - adciona ao final da lista
# extend - faz extensão ha outra lista mas se mudar a atual
# insert(indice, valor_a_ser_inserido) - adicona um item na lista
# pop - extrai um intem da lista
# remove - remove um item da lista
# del - remove um faixa de valores recebe um indice inicial e um indice final
# clear - limpa lista
# sort - ordena uma lista em crescente


# Código para ferificar produtos em uma lista

produtos = ['smartphone', 'mochila', 'noteboock']
estoque = [10, 5, 1,]

nome_produto = input('Insira nome do produto: ').lower()
if nome_produto in produtos:
    i = produtos.index(nome_produto)
    quantitade_estoque = estoque[i]
    print('Produto: {} Quantidade: {}'.format(nome_produto, quantitade_estoque))
else:
    print('{} não existe no estoque'.format(nome_produto).upper())
    


