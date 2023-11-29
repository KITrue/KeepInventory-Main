# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from math import sqrt


data = pd.date_range('2022-01-01', '2023-01-01', freq='D')
stock = np.random.randint(50, 100, size=(len(data)))

df = pd.DataFrame({'data': data, 'estoque': stock})

df['data'] = pd.to_datetime(df['data'])
df.set_index('data', inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(df, label='Estoque Real')
plt.title('Dados de Estoque')
plt.legend()
plt.show()

train_size = int(len(df) * 0.8)
train, test = df[:train_size], df[train_size:]

order = (1, 1, 1)  # Ordem do ARIMA
seasonal_order = (1, 1, 1, 12)  # Ordem sazonal do ARIMA

model = SARIMAX(train, order=order, seasonal_order=seasonal_order, enforce_stationarity=False, enforce_invertibility=False)
result = model.fit(disp=False)

# Fazer previsões
start = len(train)
end = len(train) + len(test) - 1
predictions = result.predict(start=start, end=end, dynamic=False, typ='levels')

# Visualizar os resultados
plt.figure(figsize=(10, 6))
plt.plot(train, label='Treino')
plt.plot(test, label='Teste')
plt.plot(predictions, label='Previsões')
plt.title('Previsão de Estoque com SARIMA')
plt.legend()
plt.show()# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from math import sqrt

# Carregando os dados de estoque (substitua isso pelo seu conjunto de dados real)
# Certifique-se de ter uma coluna de data (datetime) e outra com os valores de estoque.
# Vamos chamar essas colunas de 'data' e 'estoque' para fins de exemplo.

# Exemplo de leitura de dados CSV:
# df = pd.read_csv('seuarquivo.csv')
# OU
# Exemplo de criação de dados fictícios:
data = pd.date_range('2022-01-01', '2023-01-01', freq='D')
stock = np.random.randint(50, 100, size=(len(data)))

df = pd.DataFrame({'data': data, 'estoque': stock})

# Converter a coluna de data para o tipo datetime e defini-la como índice
df['data'] = pd.to_datetime(df['data'])
df.set_index('data', inplace=True)

# Visualizar os dados
plt.figure(figsize=(10, 6))
plt.plot(df, label='Estoque Real')
plt.title('Dados de Estoque')
plt.legend()
plt.show()

# Dividir os dados em treino e teste (por exemplo, 80% treino, 20% teste)
train_size = int(len(df) * 0.8)
train, test = df[:train_size], df[train_size:]

# Treinar o modelo SARIMA
order = (1, 1, 1)  # Ordem do ARIMA
seasonal_order = (1, 1, 1, 12)  # Ordem sazonal do ARIMA

model = SARIMAX(train, order=order, seasonal_order=seasonal_order, enforce_stationarity=False, enforce_invertibility=False)
result = model.fit(disp=False)

# Fazer previsões
start = len(train)
end = len(train) + len(test) - 1
predictions = result.predict(start=start, end=end, dynamic=False, typ='levels')

# Visualizar os resultados
plt.figure(figsize=(10, 6))
plt.plot(train, label='Treino')
plt.plot(test, label='Teste')
plt.plot(predictions, label='Previsões')
plt.title('Previsão de Estoque com SARIMA')
plt.legend()
plt.show()

# Avaliar o desempenho do modelo
rmse = sqrt(mean_squared_error(test, predictions))
print(f'Raiz do Erro Quadrático Médio (RMSE): {rmse}')


# Avaliar o desempenho do modelo
rmse = sqrt(mean_squared_error(test, predictions))
print(f'Raiz do Erro Quadrático Médio (RMSE): {rmse}')
