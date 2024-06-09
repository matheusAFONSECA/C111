import pandas as pd                     # importação da biblioteca do pandas
import matplotlib.pyplot as plt         # sub-biblioteca do matplotlib

# leitura do dataframe 'space.csv'
df = pd.read_csv('space.csv', delimiter=';')       # carregando um aquivo '.csv' com pandas

# filtrando as linhas onde a localização contém "USA" e "China"
usa_empresas = df[df['Location'].str.contains('USA')]
china_empresas = df[df['Location'].str.contains('China')]
# print(usa_empresas)
# print(china_empresas)

# contando quantas empresas existem em cada pais de forma únicas
usa_empresas_unicas = usa_empresas['Company Name'].unique()
china_empresas_unicas = china_empresas['Company Name'].unique()
# print(usa_empresas_unicas)
# print(china_empresas_unicas)

# Número de empresas únicas
num_usa = len(usa_empresas_unicas)
num_china = len(china_empresas_unicas)

# Plotar o gráfico de barras
countries = ['USA', 'China']            # Nome das empresas - eixo X
empresas = [num_usa, num_china]         # numero total das empresas de cada país - eixo Y

# configurar o tamanho do gráfico
plt.figure(figsize=(8, 6))

# configurar as barras do gráfico
plt.bar(countries, empresas, color=['blue', 'red'])

# configurar os eixos e rotulos
plt.xlabel('País')
plt.ylabel('Número de empresas')
plt.title('Número de empresas espaciais nos USA e China')

# mostrar o gráfico
plt.show()
