import numpy as np          # importação da biblioteca NumPy

# criando uma matriz de 1 de tamanho 3x3
arr = np.ones((3, 4))
print(arr)

# extraindo o número de linhas e colunas
linhas, colunas = arr.shape
print(linhas)
print(colunas)

# multiplicando o numero de linhas e colunas
mult = linhas * colunas

# definindo se o vetor dessa matriz poderia ser de uma quantidade par ou impar
if mult % 2 == 0:
    print("PAR")
else:
    print("IMPAR")
