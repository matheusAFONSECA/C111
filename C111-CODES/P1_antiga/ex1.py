import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

arr_slicing = arr[1:, 0:4]

print(arr_slicing)
