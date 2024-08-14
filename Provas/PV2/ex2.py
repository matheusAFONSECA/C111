import pandas as pd                 # carrega a biblioteca do pandas
import matplotlib.pyplot as plt     # carrega a biblioteca do matplotlib

# carregando o arquivo .csv como dataframe usando pandas
df = pd.read_csv('world_happiness.csv', delimiter=',')

# selecionando os 20 países mais infelizes
infelizes = df['Ladder score'].nsmallest(20)

# plotando o gráfico de pizza
plt.title("Os vinte países mais infelizes do mundo")
plt.pie(x=infelizes, labels=df['Country name'].tail(20))
plt.show()
