import pandas as pd                 # carrega a biblioteca do pandas
import matplotlib.pyplot as plt     # carrega a biblioteca do matplotlib

# carregando o arquivo .csv como dataframe usando pandas
df = pd.read_csv('world_happiness.csv', delimiter=',')

# pegando o valor de "liberdade de se fazer escolhas de vida" do brasil e america latina/caribe
brasil = df[df['Country name'].str.contains('Brazil')]
america_caribe_vida = df[df['Regional indicator'].str.contains('Latin America and Caribbean')]
# print(america_caribe_vida['Freedom to make life choices'].mean())
# print(brasil['Freedom to make life choices'])

valores_x = ['Brasil', 'America latina e Caribe']
valores_y = [float(brasil['Freedom to make life choices'].iloc[0]), america_caribe_vida['Freedom to make life choices'].mean()]


# plotando o gráfico de barras
plt.xlabel('Países')
plt.ylabel("liberdade de se fazer escolhas de vida")
plt.title("Liberdade de se fazer escolhas de vida")
plt.bar(valores_x, valores_y, color='green')
plt.show()
