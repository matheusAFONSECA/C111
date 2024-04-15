import numpy as np      # importação da biblioteca de Numpy

# carregando o arquivo .csv para uma numpy array
arr = np.loadtxt('brands.csv', delimiter=';', dtype=str, encoding='utf-8')

# arr_USA = len(arr[np.char.find(arr[:, 3], 'United States') >= 0])   # quantidade de empresas fundadas nos USA
# arr_empresas = len(arr[1:, 3])                                      # total de empresas

# porcentagem de empresas fundadas nos USA
arr_empresas_USA = (len(arr[np.char.find(arr[:, 3], 'United States') >= 0]) / len(arr[1:, 3])) * 100

print(f"São {arr_empresas_USA}% do total de empresas deste dataset que são dos Estados Unidos")
