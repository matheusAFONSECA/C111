import numpy as np          # importação da biblioteca NumPy

# criando uma matriz de 1 de tamanho 3x4
arr = np.ones((3, 4))
print(arr)

# transformando em 1-D
arr1 = arr.reshape(1, 12)
print(arr1)
