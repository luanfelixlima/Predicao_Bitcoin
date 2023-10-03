import pandas as pd
from datetime import timedelta

print(f"\n\n{'-'*20} Preparando Dados {'-'*20}")

""" CARREGANDO DADOS """
url = 'https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv'
raw_data = pd.read_csv(url, low_memory=False)

dados = raw_data[['time', 'PriceUSD']]
print("Dados \"Crus\":")
print(raw_data.head(), '\n')

""" LIMPANDO DADOS """
print("Dados que vamos usar:")
print(dados.head(), "\n")
print("Linhas e colunas antes da limpeza:", dados.shape)

dados = dados.dropna()
print("Linhas e colunas removendo valores nulos:", dados.shape)  # antes não havia btc

""" PREPARANDO DADOS """
# Verificando os tipos de dados
print("\nTipo de dados no DF (antes da conversão):\n", dados.dtypes, "\n")

# Alterando o tipo de dados da coluna "time"
dados['time'] = pd.to_datetime(dados['time'])
print("Tipo de dados no DF (depois da conversão):\n", dados.dtypes, "\n")

# Separando o dia, mes e ano da data, preparando para a reglin
dados['dia'] = dados['time'].dt.day
dados['mes'] = dados['time'].dt.month
dados['ano'] = dados['time'].dt.year
dados['Preco'] = dados['PriceUSD']

# Dados que iremos usar para regressão (dados reais)
dados_regressao = dados[['dia', 'mes', 'ano', 'Preco']]
dias = 15 # Quantidade de dias que usaremos para pegar os dados para treinar o modelo
meses = 0 # Quantidade de meses que usaremos para pegar os dados para treinar o modelo
anos = 0 # Quantidade de anos que usaremos para pegar os dados para treinar o modelo
soma_tempo = ((anos * 365) + (meses * 31) + dias)
dados_regressao = dados_regressao.tail(soma_tempo) 
print("Dados prontos para experimentos:")
print(dados_regressao)

# Criando novos valores para predições (x dias para frente)
last_date = list(dados['time'].tail(1))  # pegando a última data
datas_futuras = []
dias_prever = 3

# Loop add dias
for i in range(1, dias_prever + 1):  # somando de 1 a 10 dias na última data do df
    dia_add = timedelta(days=i)
    datas_futuras.append(last_date[0] + dia_add)

# Criando novo DF com as futuras datas
# print("novos valores de x:\n", datas_futuras, "\n")
print(f"\nDados para testes ({dias_prever} dias):")
datas_futuras = {'DatasFuturas': datas_futuras}

datas_futuras = pd.DataFrame(datas_futuras)
datas_futuras['dia'] = datas_futuras['DatasFuturas'].dt.day
datas_futuras['mes'] = datas_futuras['DatasFuturas'].dt.month
datas_futuras['ano'] = datas_futuras['DatasFuturas'].dt.year
print(datas_futuras)
