import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

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

# Plotando gráficos para entender os dados
datas = list(dados['time'])
valores = list(dados['PriceUSD'])
anos = []  # armazenando somente os anos das datas para melhor visualização no gráfico de barras
for data in datas:
    anos.append(data.year)

# Grafico de linha
plt.plot(datas, valores)
plt.xlabel("Anos")
plt.ylabel("Preço (USD)")
plt.title("Valor do Bitcoin x Ano")
plt.show()

# Grafico de barra
plt.bar(anos, valores)
plt.xlabel("Anos")
plt.ylabel("Preço (USD)")
plt.title("Valor do Bitcoin x Ano")
plt.show()

# Grafico de pontos
plt.scatter(datas, valores)
plt.xlabel("Anos")
plt.ylabel("Preço (USD)")
plt.title("Valor do Bitcoin x Ano")
plt.show()

