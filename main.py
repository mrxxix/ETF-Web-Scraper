'''
Made by: https://github.com/mrxxix

Descrição: Este script em Python permite consultar e visualizar dados históricos do ETF JEPI
(JPMorgan Equity Premium Income) através da API oficial da NASDAQ. O utilizador pode indicar
quantos resultados deseja ver (entre 1 e 250), sendo os dados apresentados numa tabela
formatada com o auxílio da biblioteca pandas.

Inclui verificação de input, controlo de erros e acesso direto à API de forma simples e
eficaz. 
'''

import requests
import pandas as pd
import sys

# Função com consequências do input do utilizador
def getUserInput():
    while True:
        numResults = input('Resultados a apresentar (1-250) ou "exit" para sair: ').strip()

        if numResults.lower() == "exit":
            print("Programa terminado pelo utilizador.")
            sys.exit()

        try:
            numResults = int(numResults)  # Valor inteiro
            if 1 <= numResults <= 250:    # Valor inteiro dentro dos limites
                print(f"A mostrar {numResults} resultados.")
                return numResults
            else:                         # Valor inteiro fora dos limites
                print(f"Erro: Número excede os limites permitidos (1-250). Inseriu: {numResults}.")
                
        except ValueError:                # Valor não inteiro
            print("Erro: Insira um número inteiro válido ou escreva 'exit' para sair.")

# Cabeçalhos necessários para evitar bloqueios da API
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Obter número de resultados
numResults = getUserInput()

# URL da API do histórico
urlHistorical = "https://api.nasdaq.com/api/quote/JEPI/historical"
paramsHistorical = {
    "assetclass": "etf",
    "fromdate": "2024-06-03",
    "todate": "2025-06-03",
    "limit": numResults
}

# Fazer o pedido
response = requests.get(urlHistorical, headers=headers, params=paramsHistorical)

# Converter para JSON
data = response.json()

# Extrair as linhas da tabela
rows = data['data']['tradesTable']['rows']

# Criar um DataFrame com pandas
dataFrame = pd.DataFrame(rows)

# Mostrar a tabela
print(dataFrame)

