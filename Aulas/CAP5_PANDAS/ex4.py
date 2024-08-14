import pandas as pd     # biblioteca Pandas

# lendo o arquivo .csv
csv = pd.read_csv('paises.csv', delimiter=';')

# Visualizando os países que não possuem costa marinha
# sem_costa_marinha = csv[csv['Coastline (coast/area ratio)'] == 0].iloc[:, 0:1]
# print(sem_costa_marinha)

# Salvando em um arquivo csv os países que não possuem costa marinha
csv[csv['Coastline (coast/area ratio)'] == 0].iloc[:, 0:1].to_csv('noCoast.csv', sep=';')
