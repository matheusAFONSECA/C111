import pandas as pd     # biblioteca Pandas

# lendo o arquivo .csv
csv = pd.read_csv('paises.csv', delimiter=';')

# Cabeçalho dos dados
# print(csv.head(0))

# Determinando quais os páises da oceania
paises = csv[csv['Region'] == 'OCEANIA                            '].iloc[:, 0:1]

# A
print("Países da Oceania: ")
print(paises)

# B
# print(f"Quantidade de países da Oceania: {len(paises)}")
print(f"Quantidade de países da Oceania: {paises.size}")
