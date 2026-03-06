import matplotlib.pyplot as plt
import ast

# Entrando com valores para o gráfico de linhas
lista=input("Entre com os valores de x em uma lista: ")
x=ast.literal_eval(lista)       # converte em uma lista
lista=input("Entre com os valores de y em uma lista: ")
y=ast.literal_eval(lista)       # converte em uma lista

# Entrando com valores para o gráfico de barras
lista=input("Entre com as categorias: ")
categorias=ast.literal_eval(lista) # converte em uma lista
lista=input("Entre com os valores das categorias: ")
valores=ast.literal_eval(lista)    # converte em uma lista

plt.figure("Gráfico de Linha")  # Cria uma nova janela para plotagem
plt.plot(x,y,color='blue')      # plotando x no eixo horizontal
                                # e y no eixo vertical
plt.title("Gráfico de Linha")   # título do gráfico
plt.xlabel("Eixo X")            # nome do eixo x (eixo horizontal)
plt.ylabel("Valores em y")      # nome do eixo y (eixo vertical)
plt.grid(False)                 # desenha as grades do gráfico
plt.show()                      # Exibe a primeira janela

plt.figure("Gráfico de Barras") # Nova janela separada
plt.bar(categorias,valores,color='green') # gera o gráfico de barras
plt.title("Gráfico de Barras")
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.show()                       # Exibe a segunda janela




