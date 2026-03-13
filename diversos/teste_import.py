import engenharia   # importanto funções

# importanto algumas funções específicas
# from engenharia import exibe, areacirculo

r=float(input("Entre com o raio da esfera para calcular o volume: "))
volume=engenharia.vol_esfera(r)
engenharia.exibe(volume)
