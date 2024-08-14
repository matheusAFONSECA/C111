import numpy as np      # importação da biblioteca de Numpy

# carregando o arquivo .csv para uma numpy array
arr = np.loadtxt('brands.csv', delimiter=';', dtype=str, encoding='utf-8')

# Realizando o Slicing no dataset
arr_slicing = arr[1:, 0:3]

# Array das empresas fundadas após os anos 2000
arr_empresas_2000 = arr_slicing[arr_slicing[:, 2].astype(float) > 2000][:, 0]

print(f"As empresas fundadas após os anos 2000 são: {arr_empresas_2000}")
