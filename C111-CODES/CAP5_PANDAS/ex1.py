import pandas as pd     # biblioteca Pandas

# lendo o arquivo .csv
csv = pd.read_csv('paises.csv', delimiter=';')

paises = csv[csv['Region'] == 'OCEANIA']

print(paises)
