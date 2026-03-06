import os

inputsenha = input("Digite a senha: ")

with open("senhaInvestimento.txt","r") as arquivo:
    senha = arquivo.read()
    

if inputsenha == senha :
      print("\nAcesso liberado, Bem-vindo!")
      
      opcao = int(input("\nOpcoes disponiveis: \n1-Mudar a senha\n2-Calcular imposto\n\nEscolha a opcao desejada: "))
      if opcao == 1 :
            novaSenha = input("Digite a nova senha: ")
            with open("senhaInvestimento.txt","w") as arquivo:
             arquivo.write(novaSenha)      
             print("\nSenha alterada com sucesso")
          
            
            
      elif opcao == 2 :
            print("\nEste programa calcula o imposto sobre o rendimentos de acordo com a tabela")
            dias = int(input("Entre com o tempo em dias: "))
            dinheiro = int(input("Entre com os rendimentos em reais: "))
            if dias <= 180  :
                  calculo = dinheiro * 0.225
                  print(calculo)
            elif dias >= 181 and dias <=360 :
                  calculo = dinheiro * 0.20
                  print(calculo)
            elif dias >= 361 and dias <=720 :
                  calculo = dinheiro * 0.175
                  print(calculo)
            else:
                  calculo = dinheiro * 0.15
                  print(calculo)
      else:
            print("Opcao invalida, acesso finalizado")
    
else :
      print("Senha invalida, Acesso negado")
    

       