import matplotlib.pyplot as plt

valor = float(input("Entre com o valor inicial da aplicação: "))
meses = int(input("Entre com a quantidade de meses: "))

listaMeses=[]
listaJuros= []

taxa = 0.015  

for mes in range(1, meses + 1):
    taxaJuros = valor * taxa
    valor = valor + taxaJuros
    
    listaJuros.append(round(taxaJuros, 2))
    listaMeses.append(mes)
    print("Mês" + str(mes) + ": Rendimento=" + str(round(taxaJuros,2)) + " Total aplicado=" + str(valor))

plt.figure("Gráfico de Barras") 
plt.bar(listaMeses,listaJuros,color='green') 
plt.title("Gráfico de Barras")
plt.xlabel("Meses")
plt.ylabel("Juros")
plt.show()       