import numpy as np          # importação da biblioteca NumPy

np.random.seed(5)   # determinando a "seed" para a seleção dos n° aleatórios

arr = np.random.randn(10)          # cria uma array de floats com 10 elementos positivos e negativos entre 0 e 1
print(f"A array original é: {arr}")

arr = arr*100               # multiplicando os valores por 100
arr2 = arr.astype(int)      # pegando somente a parte inteira dos valores
print(f"A array modificada é: {arr2}")
