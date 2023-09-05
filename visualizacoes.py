import matplotlib.pyplot as plt
from main import dados

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
