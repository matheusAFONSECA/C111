import pandas as pd     # biblioteca Pandas

# lendo o arquivo .csv
csv = pd.read_csv('paises.csv', delimiter=';')

# Encontrando país e região com a maior população
maior_populacao = csv.loc[csv['Population'].idxmax(), ['Country', 'Region', 'Population']]
# print(maior_populacao)

print(f"País, com sua respectiva região, com a maior população: {', '.join(map(str, maior_populacao))}")


