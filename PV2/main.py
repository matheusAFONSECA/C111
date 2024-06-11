import pandas as pd                 # carrega a biblioteca do pandas
import matplotlib.pyplot as plt     # carrega a biblioteca do matplotlib

# carregando o arquivo .csv como dataframe usando pandas
df = pd.read_csv('world_happiness.csv', delimiter=',')

# EX1
# plotando o gráfico de barras
plt.xlabel('Países')
plt.ylabel("Expectativa de vida saudável")
plt.title("Os cinco países com maior expectativa de vida saudável")
plt.bar(df['Country name'].head(), df['Healthy life expectancy'].nlargest(), color='green')
plt.show()


# EX2
# selecionando os 20 países mais infelizes
infelizes = df['Ladder score'].nsmallest(20)

# plotando o gráfico de pizza
plt.title("Os vinte países mais infelizes do mundo")
plt.pie(x=infelizes, labels=df['Country name'].tail(20))
plt.show()

# EX3
# selecionando os paises da america latina e caribe
america_caribe = df[df['Regional indicator'].str.contains('Latin America and Caribbean')]
# print(america_caribe)

# plotando um scatter plot
plt.xlabel('Países')
plt.ylabel("Pontuação de felicidade")
plt.title("Os cinco países mais felizes da America Latina e Caribe")
plt.scatter(america_caribe['Country name'].head(), america_caribe['Ladder score'].nlargest())
plt.show()

# EX4
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
