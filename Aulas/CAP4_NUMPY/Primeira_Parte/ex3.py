import numpy as np          # importação da biblioteca NumPy
# criando uma array com valores pares entre 0 à 51
arr1 = np.arange(0, 51, 2)

# criando uma array com valores pares entre 100 à 50
arr2 = np.arange(100, 50, -2)

# concatenando os valores dos arrays
arr = np.concatenate([arr1, arr2])

# ordenando os valores
arr_ordenada = np.sort(arr)

# ordenando em ordem decrescente
arr_decrescente = np.sort(arr_ordenada)[::-1]
print(arr_decrescente)
