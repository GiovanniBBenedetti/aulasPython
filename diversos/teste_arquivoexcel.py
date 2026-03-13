# Para manipular planilhas em Excel, devemos instalar a biblioteca:
# pip install pandas openpyxl

import pandas as pd
import os
from pathlib import Path

# Lê o arquivo Excel
tabela=pd.read_excel("tabela.xlsx")

# Mostra as 5 primeiras linhas
print(tabela.head())

# mostra toda a tabela
print(tabela.to_string())

# convertendo para uma matriz
matriz=tabela.values.tolist()

# exibe linha 0 coluna 1
print(matriz[0][1])

# quando convertemos para uma matriz,
# os títulos das colunas (os cabeçalhos) não são incluídos, só os dados das linhas.

titulos=tabela.columns.tolist()  # obtendo os títulos das colunas
print(titulos)

# gravando no arquivo excel
dados =[[1,10.5,15.55],
        [2,11.5,17.8],
        [3,12.8,20.8]]    # dados

colunas=["Tempo", "Temperatura", "Pressão"]  # títulos das colunas

# Criando o DataFrame
dados_excel=pd.DataFrame(dados,columns=colunas)

# Salva no Arquivo Excel
dados_excel.to_excel("dados_maquina.xlsx",index=False)
# Isso cria (ou sobrescreve) um arquivo dados.xlsx com as três colunas e linhas.
# Index=False faz com que o
# o Pandas não grava a coluna de índice, só os dados reais da tabela.

# verificando se o arquivo existe

if os.path.exists("dados_maquina.xlsx"):
    print("O arquivo Excel já existe.")
else:
    print("O arquivo Excel ainda não existe.")

# Usando pathlib (forma moderna e mais elegante)
arquivo = Path("dados_maquina.xlsx")

if arquivo.exists():
    print("O arquivo Excel já existe segundo pathlib.")
else:
    print("O arquivo Excel ainda não existe segundo pathlib.")