import math
velocidadeInicial =  float(input("Digite a velocidade inicial: "))
aceleracao = float(input("Digite a aceleracao: "))
deslocamento = float(input("Digite o deslocamento: "))

calculo = (velocidadeInicial **2) + (2 * aceleracao * deslocamento)
raiz = math.sqrt(calculo)
resultadoMS = raiz
resultadoKM = raiz * 3.6

print(resultadoMS)
print(resultadoKM)  