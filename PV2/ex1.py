import pandas as pd                 # carrega a biblioteca do pandas
import matplotlib.pyplot as plt     # carrega a biblioteca do matplotlib

# carregando o arquivo .csv como dataframe usando pandas
df = pd.read_csv('world_happiness.csv', delimiter=',')

# plotando o gráfico de barras
plt.xlabel('Países')
plt.ylabel("Expectativa de vida saudável")
plt.title("Os cinco países com maior expectativa de vida saudável")
plt.bar(df['Country name'].head(), df['Healthy life expectancy'].nlargest(), color='green')
plt.show()
