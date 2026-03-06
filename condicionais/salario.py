salario = float(input("Entre com o salario bruto: "))

if salario <=2000:
    print("Imposto 0")
elif salario >= 2000.01 and salario <= 4000.00:
    calculo =(0.1 * salario) - 200
    print("Imposto:"+ str(calculo))
elif salario >= 4000.01 and salario <= 6000.00:
    calculo = (0.2 * salario)-600
    print("Imposto:"+ str(calculo))
else :
    calculo = (0.3 * salario) - 1200
    print("Imposto:"+ str(calculo))