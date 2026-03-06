import math

catetoOposto=float(input("Digite o catesto oposto: "))
catetoAdjascente=float(input("Digite o catesto oposto: "))

calculo = (catetoOposto ** 2 + catetoAdjascente**2)
raiz =  math.sqrt(calculo)

print(raiz)