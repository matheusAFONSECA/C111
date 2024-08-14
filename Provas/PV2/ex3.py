import pandas as pd                 # carrega a biblioteca do pandas
import matplotlib.pyplot as plt     # carrega a biblioteca do matplotlib

# carregando o arquivo .csv como dataframe usando pandas
df = pd.read_csv('world_happiness.csv', delimiter=',')

# selecionando os paises da america latina e caribe
america_caribe = df[df['Regional indicator'].str.contains('Latin America and Caribbean')]
# print(america_caribe)

# plotando um scatter plot
plt.xlabel('Países')
plt.ylabel("Pontuação de felicidade")
plt.title("Os cinco países mais felizes da America Latina e Caribe")
plt.scatter(america_caribe['Country name'].head(), america_caribe['Ladder score'].nlargest())
plt.show()

