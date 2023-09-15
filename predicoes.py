from sklearn.linear_model import LinearRegression
from preparacao_dados import *

print(f"\n\n{'-'*20} Experimentos e Predições {'-'*20}")

# Dados para treino
x = dados_regressao[['dia', 'mes', 'ano']]
y = dados_regressao['Preco']

# Treinando
modelo = LinearRegression()
modelo.fit(x, y)

# Dados para teste
x_test = datas_futuras[['dia', 'mes', 'ano']]

# Testando
y_pred = modelo.predict(x_test)

# Resultados
datas_res = list(datas_futuras['DatasFuturas'])
df_pred = pd.DataFrame({'Data': datas_res, 'Preco': y_pred})
print("Previsão de preços:")
print(df_pred)
