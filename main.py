import pandas as pd
import numpy as np
from datetime import timedelta
from sklearn.linear_model import LinearRegression

# Carregando dados
url = 'https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv'
raw_data = pd.read_csv(url, low_memory=False)

dados = raw_data[['time', 'PriceUSD']]
print("Dados \"Crus\":")
print(raw_data.head(), '\n')

# Limpeza dados
print("Dados que vamos usar:")
print(dados.head(), "\n")
print("Linhas e colunas antes da limpeza:", dados.shape)

dados = dados.dropna()
print("Linhas e colunas removendo valores nulos:", dados.shape)  # antes não havia btc

# Verificando os tipos de dados
print("\nTipo de dados no DF (antes da conversão):\n", dados.dtypes, "\n")

# Alterando o tipo de dados da coluna "time"
dados['time'] = pd.to_datetime(dados['time'])
print("Tipo de dados no DF (depois da conversão):\n", dados.dtypes, "\n")

""" Experimentos e Predições """
# Carregando os dados para utilizar na regressão
x = np.array(dados['time'])  # possível erro: tipo de dados: datas
x = x.reshape(-1, 1)
y = np.array(dados['PriceUSD'])

# Criando e ajustando o modelo
modelo = LinearRegression()
modelo.fit(x, y)

# Criando novos valores para a predição (10 dias para frente)
last_date = list(dados['time'].tail(1))  # pegando a última data
datas_futuras = []

# Loop add dias
for i in range(1, 11):  # somando de 1 a 10 dias na última data do df
    dia_add = timedelta(days=i)
    datas_futuras.append(last_date[0] + dia_add)

print("novos valores de x:\n", datas_futuras, "\n")
datas_futuras = {'DatasFuturas': datas_futuras}

datas_futuras = pd.DataFrame(datas_futuras)
