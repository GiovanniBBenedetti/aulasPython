    import ast
    import matplotlib.pyplot as plt

    valorInicial = float(input("Digite o valor inicial da aplicacao: "))
    listaRentabilidade = input("Digite a lista de rentabilidade: ")

    valor = valorInicial
    listaMeses=[]
    listaJuros= []

    valores = ast.literal_eval(listaRentabilidade)
    tamanhoLista = len(valores)

    for mes in range(tamanhoLista):

        rendimento_percentual = valores[mes]
        taxa = rendimento_percentual / 100
        
        rendimento = valor * taxa
        valor = valor + rendimento
        
        
        imposto = 0

        if rendimento_percentual > 1.5:
            imposto = valor * (rendimento_percentual - 1.5) * 0.001
            valor = valor - imposto
            
        listaJuros.append(round(valor, 2))
        listaMeses.append(mes)

        print("Mes", mes + 1, "Rendimento =", round(rendimento,2), "Total aplicado =", round(valor,2))
        
        
    plt.figure("Gráfico de Barras") 
    plt.bar(listaMeses,listaJuros,color='green') 
    plt.title("Gráfico de Barras")
    plt.xlabel("Meses")
    plt.ylabel("Juros")
    plt.show()      