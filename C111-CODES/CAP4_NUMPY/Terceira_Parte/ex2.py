import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('..\\space.csv', delimiter=';', dtype=str, encoding='utf-8')
arr = np.delete(arr, 0, axis=0)     # deletando o cabeçalho da array

# Selecionando apenas as linhas onde o valor na coluna 6 é maior que 0 e convertendo os valores para float e, em seguida
# convertendo a array resultante em float
arr_custos = arr[arr[:, 6].astype(float) > 0][:, 6].astype(float)

# print(len(arr_custos))            # quantidade de viagens com o custo acima de 0
# print(np.sum(arr_custos))         # soma dos custos das viagens com o custo acima de 0
print(f"A média de custos das viagens são: {(np.sum(arr_custos) / len(arr_custos)):.2f}")
