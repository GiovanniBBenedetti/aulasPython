import os
import hashlib

user1_nome = "ana"
user1_hash = "12313a3d28f802e3a22b07d2e01c6dcf"

user2_nome = "bia"
user2_hash = "f8dbbbdb3b80b4f170a8272978f579eb"

user3_nome = "caio"
user3_hash = "5fa9db2e335ef69a4eeb9fe7974d61f4"

user4_nome = "caio"
user4_hash = "c303183db8ccee2fb0a2f5ca6c030f68"

user5_nome = "leo"
user5_hash = "bea0184aac2ef216c834b3e24a88c38e"


inputUsuario = input("Digite seu usuario: ")
inputSenha = input("Digite a senha: ")

hash_digitado = hashlib.md5(inputSenha.encode()).hexdigest()



    
acesso_concedido = False

if inputUsuario == user1_nome and hash_digitado == user1_hash:
      acesso_concedido = True
elif inputUsuario == user2_nome and hash_digitado == user2_hash:
      acesso_concedido = True
elif inputUsuario == user3_nome and hash_digitado == user3_hash:
      acesso_concedido = True
elif inputUsuario == user4_nome and hash_digitado == user4_hash:
      acesso_concedido = True


if acesso_concedido == True :
      print("\nAcesso liberado! Bem-vindo(a), " + usuario_digitado + "!")

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

else :
      print("Senha ou usuarios invalidos, Acesso negado")
    

       