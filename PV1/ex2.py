import numpy as np      # importação da biblioteca de Numpy

# carregando o arquivo .csv para uma numpy array
arr = np.loadtxt('brands.csv', delimiter=';', dtype=str, encoding='utf-8')

# Empresas que começam com a letra A
arr_empresAs = arr[np.char.find(arr[:, 0], 'A') == 0][:, 0]

print(f"Todas as empresas que começam com a letra A são: {arr_empresAs}")

arr_empresAs = np.char.upper(arr_empresAs)          # colocando todas as letras em forma maiuscula
arr_empresAs_ordenadas = arr_empresAs.sort()        # ordenando as empresas

print(f"Todas as empresas que começam com a letra A mostradas de forma ordenada são: {arr_empresAs}")

