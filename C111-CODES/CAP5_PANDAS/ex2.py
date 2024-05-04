import pandas as pd     # biblioteca Pandas

# lendo o arquivo .csv
csv = pd.read_csv('paises.csv', delimiter=';')

alfabetizacao = csv['Literacy (%)'].mean()

print(f"A média da taxa de alfabetização(Literacy) dos países é: {alfabetizacao:.2f} %")
