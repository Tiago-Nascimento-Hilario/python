import webbrowser
import time
import matplotlib.pyplot as plt

site = input('Informe link do site: ').lower()
webbrowser.open(site)

data_hoje = time.ctime()
print(data_hoje)

print('Aguardando......')
intervalo_10_segundos = time.sleep(10)
print("concluído")

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
vendas_meses = [15, 1727, 1350, 999, 10, 27, 50, 200, 33, 210, 62, 10]

plt.plot(meses, vendas_meses, color='red')
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 12, 0, max(vendas_meses)+500])
plt.show()
