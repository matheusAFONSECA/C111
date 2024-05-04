import pandas as pd     # biblioteca Pandas

# lendo o arquivo .csv
csv = pd.read_csv('paises.csv', delimiter=';')

# Cabeçalho dos dados
# print(csv.head(0))

# Exercício 1
# Determinando quais os páises da oceania
paises = csv[csv['Region'] == 'OCEANIA                            '].iloc[:, 0:1]

# A
print("Países da Oceania: ")
print(paises)

# B
# print(f"Quantidade de países da Oceania: {len(paises)}")
print(f"Quantidade de países da Oceania: {paises.size}")


# Exercício 2
# Média de alfabetização dos países
alfabetizacao = csv['Literacy (%)'].mean()

print(f"A média da taxa de alfabetização(Literacy) dos países é: {alfabetizacao:.2f} %")

# Exercício 3
# Encontrando país e região com a maior população
maior_populacao = csv.loc[csv['Population'].idxmax(), ['Country', 'Region', 'Population']]
# print(maior_populacao)

print(f"País, com sua respectiva região, com a maior população: {', '.join(map(str, maior_populacao))}")

# Exercício 4
# Visualizando os países que não possuem costa marinha
# sem_costa_marinha = csv[csv['Coastline (coast/area ratio)'] == 0].iloc[:, 0:1]
# print(sem_costa_marinha)

# Salvando em um arquivo csv os países que não possuem costa marinha
csv[csv['Coastline (coast/area ratio)'] == 0].iloc[:, 0:1].to_csv('noCoast.csv', sep=';')
