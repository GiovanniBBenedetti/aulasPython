import math

coeficienteA = float(input("Digite o coeficiente A : "))
coeficienteB = float(input("Digite o coeficiente B: "))
coeficienteC = float(input("Digite o coeficiente B: "))


delta = (coeficienteB ** 2) - 4 * (coeficienteA * coeficienteC)
calculo1 = -coeficienteB + math.sqrt(delta) 
calculo2 = -coeficienteB - math.sqrt(delta)  

divisao1 = calculo1 / (2 * coeficienteA)
divisao2 = calculo2 / (2* coeficienteA)

print(divisao1)

print(divisao2)