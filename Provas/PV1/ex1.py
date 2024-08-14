import numpy as np      # importação da biblioteca de Numpy

# carregando o arquivo .csv para uma numpy array
arr = np.loadtxt('brands.csv', delimiter=';', dtype=str, encoding='utf-8')

# vars que guardam os valores da microsoft em 2022 e 2021
# arr_microsoft_2022 = arr[np.char.find(arr[:, 0], 'Microsoft') >= 0][:, 9]
# arr_microsoft_2021 = arr[np.char.find(arr[:, 0], 'Microsoft') >= 0][:, 10]
# diferenca = arr_microsoft_2022.astype(float) - arr_microsoft_2021.astype(float)     # diferenca de valor de 2022 e 2021

# var que guarda o valor de diferença de valor da microsoft entre 2021 e 2022
arr_microsoft = arr[np.char.find(arr[:, 0], 'Microsoft') >= 0][:, 9].astype(float) - arr[np.char.find(arr[:, 0], 'Microsoft') >= 0][:, 10].astype(float)


print(f"A empresa Microsoft valorizou em $M: {arr_microsoft} entre 2021 e 2022")
