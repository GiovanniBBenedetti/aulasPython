posicaoInicial = float(input("Digite a posicao inicial: "))
velocidadeConstante = float(input("Digite a velocidade constante: "))
tempoDecorrido = float(input("Digite o tempo decorrido: "))
aceleracao = float(input("Digite o valor da aceleracao"))

calculo =  posicaoInicial + velocidadeConstante * tempoDecorrido + aceleracao * tempoDecorrido**2/2
print(calculo)