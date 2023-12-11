import pandas as pd

# selecionar linhas exemplo[:4]


cadastro_produtos_df = pd.read_csv(r'/home/tiago/dev/python/02-csv/Contoso - Cadastro Produtos.csv', sep=';')
vendas_df = pd.read_csv(r'/home/tiago/dev/python/02-csv/Contoso - Vendas  - 2017.csv', sep=';')
cliente_df = pd.read_csv(r'/home/tiago/dev/python/02-csv/Contoso - Clientes.csv', sep=';')
promocoes_df = pd.read_csv(r'/home/tiago/dev/python/02-csv/Contoso - Lojas.csv', sep=';')


print(vendas_df)
frequencia_vendas = vendas_df['Quantidade Vendida'].value_counts()
frequencia_vendas




# df_data_venda = vendas_df[['Data da Venda', 'Data do Envio', 'ID Produto']]
# df_data_venda
