import math

numero = float(input("Operacões dísponiveis :\n 1-Volume da esfera\n 2-Volume do cilindro\n 3-Volume do paralelepipedo\n 4-Volume do cone \n\nDigite qual operacao deseja: "))

if numero == 1 :
    raio = float(input("\nDigite o raio da esfera: "))
    calculo = (4/3)*math.pi*raio**3
    print("Volume da esfera: "+ str(calculo))
elif numero == 2 :
    raio = float(input("\nDigite o raio do cilindro: "))
    altura = float(input("Digite a altura do cilindro: "))
    calculo = math.pi*raio**2*altura
    print("Volume do cilindro: "+ str(calculo))
elif numero == 3 :
     comprimento = float(input("\nDigite o comprimento do retangulo: "))
     altura = float(input("Digite a altura do retangulo: "))
     largura = float(input("Digite a largura do retangulo: "))
     calculo = comprimento * altura * largura
     print("Volume do retangulo: "+ str(calculo))
elif numero == 4 :
     raio = float(input("\nDigite o raio do cone: "))
     altura = float(input("Digite a altura do cone: "))
     calculo = (math.pi* raio**2 * altura) / 3 
     print("Volume do cone: "+ str(calculo))
else :
    print("Opcao invalida, Sistema finalizado")