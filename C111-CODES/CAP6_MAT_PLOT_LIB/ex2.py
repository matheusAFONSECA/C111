import pandas as pd                     # importação da biblioteca do pandas
import matplotlib.pyplot as plt         # sub-biblioteca do matplotlib

# leitura do dataframe 'paises.csv'
df = pd.read_csv('paises.csv', delimiter=';')       # carregando um aquivo '.csv' com pandas

# filtrando os países da américa do norte
america_do_norte = df[df['Region'] == 'NORTHERN AMERICA                   ']
# print(america_do_norte)

# pegando os valores de mortalidade(DEATHRATE) e natalidade(BIRTHRATE)
mortalidade = america_do_norte['Deathrate']
natalidade = america_do_norte['Birthrate']
paises = america_do_norte['Country']
# print(mortalidade)
# print(natalidade)
# print(paises)

# Plotando os gráficos
# Configurar o tamanho do gráfico
plt.figure(figsize=(10, 5))

# Plotar as linhas de mortalidade e natalidade
plt.plot(paises, mortalidade, marker='o', color='red', label='Mortalidade')
plt.plot(paises, natalidade, marker='o', color='blue', label='Natalidade')

# Configurar os eixos e rótulos
plt.xlabel('Países')
plt.ylabel('Taxas (%)')
plt.title('Taxas de Mortalidade e Natalidade nos Países da América do Norte')
plt.legend()

# Mostrar o gráfico
plt.show()
