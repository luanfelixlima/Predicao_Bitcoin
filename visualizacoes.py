import matplotlib.pyplot as plt
from preparacao_dados import dados
from predicoes import dados_reais_x, dados_reais_y, dados_previsto_x, dados_previsto_y

"""# Plotando gráficos para entender os dados
datas = list(dados['time'])
valores = list(dados['PriceUSD'])
anos = []  # armazenando somente os anos das datas para melhor visualização no gráfico de barras
for data in datas:
    anos.append(data.year)"""

# VISUALIZAÇÕES REAIS:

"""# Grafico de linha
plt.plot(datas, valores)
plt.xlabel("Anos")
plt.ylabel("Preço (USD)")
plt.title("Valor do Bitcoin x Ano (Valor Real)")
plt.show()

# Grafico de barra
plt.bar(anos, valores)
plt.xlabel("Anos")
plt.ylabel("Preço (USD)")
plt.title("Valor do Bitcoin x Ano (Valor Real)")
plt.show()

# Grafico de pontos
plt.scatter(datas, valores)
plt.xlabel("Anos")
plt.ylabel("Preço (USD)")
plt.title("Valor do Bitcoin x Ano (Valor Real)")
plt.show()"""

# VISUALIZAÇÕES PREDIÇÃO:
x = []
for dados in dados_reais_x:
    x.append(dados)
for dados in dados_previsto_x:
    x.append(dados)

y = []
for dados in dados_reais_y:
    y.append(dados)
for dados in dados_previsto_y:
    y.append(dados)

plt.plot(x, y)
plt.xlabel("Anos")
plt.ylabel("Preço (USD)")
plt.title("Valor do Bitcoin x Ano (Valor Real)")
plt.show()
