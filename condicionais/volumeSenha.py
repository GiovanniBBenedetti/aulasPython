import math
import os

inputSenha = input("Digite a sua senha: ")

with open("senhaVolume.txt","r") as arquivo:
    senha = arquivo.read()

if inputSenha == senha :
    opcao = int(input("\nOpcoes disponiveis: \n1-Mudar a senha\n2-Calcular volumes de figuras\n\nEscolha a opcao desejada: "))
    if opcao == 1 :
        novaSenha = input("Digite a nova senha: ")
        with open("senhaVolume.txt","w") as arquivo:
            arquivo.write(novaSenha)      # escreve a primeira linha
            print("\nSenha alterada com sucesso")
    elif opcao == 2 :
        numero = float(input("\nOperacões dísponiveis :\n 1-Volume da esfera\n 2-Volume do cilindro\n 3-Volume do paralelepipedo\n 4-Volume do cone \n\nDigite qual operacao deseja: "))

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
    else :
        print("Opcao invalida, acesso finalizado")    
           
else :
    print("Senha invalida, acesso negado")    


