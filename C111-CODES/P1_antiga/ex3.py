import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')
arr = np.delete(arr, 0, axis=0)     # deletando o cabeçalho da array

# selecionando onde a taxa de alfabetização é maior de 0 e convertendo o valor para float
arr_literacy = arr[arr[:, 9].astype(float) > 0][:, 9].astype(float)

# print(len(arr_literacy))
# print(np.sum(arr_leteracy))
print(f"A taxa de alfabetização é {(np.sum(arr_literacy) / len(arr_literacy)):.2f}%")
