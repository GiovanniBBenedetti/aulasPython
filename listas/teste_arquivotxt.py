import os
from pathlib import Path

# Abre o arquivo .txt para a escrita, se ele não existir ele é criado
# w indica que serão gravados dados
with open("testetxt.txt","w") as arquivo:
    arquivo.write("Ana\n")      # escreve a primeira linha
    arquivo.write("Paulo\n")    # escreve a segunda linha \n indica quebra de linha
    arquivo.write("Roberto\n")  # escreve a terceira linha

# "w" abre o arquivo mas apaga todo o conteúdo que foi criado antes

# com a estrutura with as, o arquivo é fechado automaticamente no final

# adicionando linhas no final ("a" indica adicionamento de linhas)
with open("testetxt.txt","a") as arquivo:
    arquivo.write("Ola.\n")
    arquivo.write("Bom dia.\n")

# lendo o arquivo de uma unica vez ("r" indica leitura)
with open("testetxt.txt","r") as arquivo:
    linhas = arquivo.read()
    print(linhas)

# r+ indica escrita e leitura no arquivo
# w+ indica escrita e leitura (apaga conteúdo anterior)
# a+ indica leitura e acrescentar

# verificando se o arquivo existe

if os.path.exists("testetxt.txt"):
    print("O arquivo já existe.")
else:
    print("O arquivo não existe.")

# Usando pathlib (recomendado em código moderno)

arquivo=Path("testetxt.txt")

if arquivo.exists():
    print("O arquivo já existe de acordo com pathlib.")
else:
    print("O arquivo não existe de acordo com pathlib.")

    
