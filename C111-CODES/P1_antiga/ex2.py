import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')
arr = np.delete(arr, 0, axis=0)     # deletando o cabeçalho da array

# selecionando a coluna das regiões e pegando os vaores unicos e depois fazendo a contagem
arr_region = len(np.unique(arr[:, 1]))

print(f"São {arr_region} regiões")
