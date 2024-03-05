import numpy as np          # importação da biblioteca NumPy

# criando uma array com valores entre 0 à 1 com espaçamente de 21
x = 1/21
arr = np.arange(0, 1, x)

print(arr)
print(arr.size)
