# Predição Bitcoin

Descrição:\
Predição realizada apenas com regressão linear, não considerando fatores externos, apenas estatística.

---

Passos:

Carregamento e Limpeza da base: 
- Carregamento da base: https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv em um DataFrame com a biblioteca Pandas.
- Removendo valores nulos em relação aos preços do bitcoin.
- Alterando tipos de dados não convenientes.

Exploração e Visualização:
- Plotando gráficos para melhor visualização da tendência dos preços ao longo dos anos.

Experimentos e Predições:
- Criar arrays para criar e treinar o modelo.
- Criar novos dados para inserir nas colunas independentes e testar o modelo.