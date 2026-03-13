def hipotenusa(x,y):  # Uma função de nome hipotenusa
                      # que recebe 2 números e calcula
                      # a hipotenusa
    return (x**2+y**2)**0.5   # retorna o valor calculado

def exibe(valor):   # rotina ou procedimento não retorna valor
    print("O valor da hipotenusa é: ")
    print(valor)
    print("Obrigado por usar o programa.")

a=float(input("Entre com o cateto a: "))
b=float(input("Entre com o cateto b: "))
hip=hipotenusa(a,b)
exibe(hip)