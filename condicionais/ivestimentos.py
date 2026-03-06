dias = int(input("Entre com o tempo em dias: "))
dinheiro = int(input("Entre com os rendimentos em reais: "))

print("Este programa calcula o imposto sobre o rendimentos de acordo com a tabela")

if dias <= 180  :
     calculo = dinheiro * 0.225
     print("Imposto (R$)= "+str(calculo))
elif dias >= 181 and dias <=360 :
     calculo = dinheiro * 0.20
     print("Imposto (R$)= "+str(calculo))
elif dias >= 361 and dias <=720 :
     calculo = dinheiro * 0.175
     print("Imposto (R$)= "+str(calculo))
else:
     calculo = dinheiro * 0.15
     print("Imposto (R$)= "+str(calculo))
    

