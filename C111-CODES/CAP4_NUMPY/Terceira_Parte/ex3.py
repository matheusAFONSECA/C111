import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('..\\space.csv', delimiter=';', dtype=str, encoding='utf-8')
arr = np.delete(arr, 0, axis=0)     # deletando o cabeçalho da array

contagem_usa = len(arr[np.char.find(arr, 'USA') >= 0])         # quantidade de missões nos USA

print(f"Quantidade de missões realizadas nos USA: {contagem_usa}")
