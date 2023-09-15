# Predição Bitcoin

Descrição:\
Predição realizada apenas com regressão linear, não considerando fatores externos, apenas estatísticos.

---
Passo a Passo:
- 

Carregamento e Limpeza da base: 
- Carregamento da base: https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv em um DataFrame com a biblioteca Pandas.
- Removendo valores nulos em relação aos preços do bitcoin.

Preparação dos dados:
- Alterando tipos de dados não convenientes.
- Destrinchando datas em números para a regressão linear. 
- Criar novos dados para inserir nas colunas independentes e testar o modelo.

Exploração e Visualização:
- Plotando gráficos para melhor visualização da tendência dos preços ao longo dos anos (valores reais).

Experimentos e Predições:
- Criar arrays para treinar e testar o modelo.
- Treinar o modelo.
- Testar o modelo.
- Visualizar os resultados.
