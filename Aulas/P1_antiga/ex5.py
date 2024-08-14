import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# Pega todos os países da america do sul e caribe(LATIN AMER. & CARIB)
arr_latin_carib = arr[np.char.find(arr[:, 1], 'LATIN AMER. & CARIB    ') >= 0]
# print(len(arr_latin_carib))   # quantidade de países da america latina e caribe

# dentre os paises da america latina e caribe, seleciona o que possui o maior GDP
arr_GDP = arr_latin_carib[arr_latin_carib[:, 8] == max(arr_latin_carib[:, 8])]

print(f"O país com o maior GDP é: {arr_GDP}")
