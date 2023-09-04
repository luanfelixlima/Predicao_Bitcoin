import pandas as pd
import matplotlib.pyplot as plt

# Carregando dados
url = 'https://raw.githubusercontent.com/coinmetrics/data/master/csv/btc.csv'
raw_data = pd.read_csv(url, low_memory=False)

print(raw_data.head())


