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
df_pred = pd.DataFrame({'Data': datas_res, 'Preco': y_pred,
                        'Data ("dados base")': dados['time'].tail(dias_prever),
                        'Preco ("dados base")': dados_regressao['Preco'].tail(dias_prever)})
print("Previsão de preços:")
print(df_pred)


# ===================== Dados para visualizações ============================ #

dados_reais_x = dados['time'].tail(soma_tempo)
dados_reais_y = dados_regressao['Preco'].tail(soma_tempo)
dados_previsto_x = datas_res
dados_previsto_y = y_pred
