import math

def areacirculo(r):        # calcula a área do círculo
    return math.pi*r**2

def hipotenusa(a,b):       # calcula a hipotenusa
    return (a**2+b**2)**0.5

def vol_esfera(r):         # calcula o volume da esfera
    return math.pi*(4/3)*r**3

def exibe(valor):          # exibe o valor
    print("O valor calculado é: ")
    print(valor)
    print("Obrigado por usar o programa")