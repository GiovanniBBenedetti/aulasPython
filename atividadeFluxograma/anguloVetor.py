import math
ax = float(input("Digite o valor de ax: "))
ay = float(input("Digite o valor de ay: "))

a = ax**2 + ay**2
raiz = math.sqrt(a)

anguloGrau  = math.atan2(ay, ax) * (180 / math.pi)

print(raiz)
print(anguloGrau)