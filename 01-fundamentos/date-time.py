from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

#Criando uma data

data_de_aniversario = datetime.strptime(input("Quando será seu aniversário: "),"%d/%m/%Y")
data_atual = datetime.now()
prazo = data_atual - data_de_aniversario
print(prazo.days)