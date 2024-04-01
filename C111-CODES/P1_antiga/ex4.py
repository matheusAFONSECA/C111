import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# quantidade de países da américa do norte
arr_north_america = len(arr[np.char.find(arr[:, 1], 'NORTHERN AMERICA                   ') >= 0])

print(f"São {arr_north_america} países da America do Norte(NORTHERN  AMERICA)")
