
inputsenha = input("Digite a senha: ")

if inputsenha == "teste" :
      print("Acesso liberado, Bem-vindo!")
      print("Este programa calcula o imposto sobre o rendimentos de acordo com a tabela")
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
else :
      print("Acesso negado")
    

       