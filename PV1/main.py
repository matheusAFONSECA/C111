import numpy as np      # importação da biblioteca de Numpy

# carregando o arquivo .csv para uma numpy array
arr = np.loadtxt('brands.csv', delimiter=';', dtype=str, encoding='utf-8')

# EX1
# vars que guardam os valores da microsoft em 2022 e 2021
# arr_microsoft_2022 = arr[np.char.find(arr[:, 0], 'Microsoft') >= 0][:, 9]
# arr_microsoft_2021 = arr[np.char.find(arr[:, 0], 'Microsoft') >= 0][:, 10]
# diferenca = arr_microsoft_2022.astype(float) - arr_microsoft_2021.astype(float)     # diferenca de valor de 2022 e 2021

# var que guarda o valor de diferença de valor da microsoft entre 2021 e 2022
arr_microsoft = arr[np.char.find(arr[:, 0], 'Microsoft') >= 0][:, 9].astype(float) - arr[np.char.find(arr[:, 0], 'Microsoft') >= 0][:, 10].astype(float)


print(f"A empresa Microsoft valorizou em $M: {arr_microsoft} entre 2021 e 2022")

# EX2
# Empresas que começam com a letra A
arr_empresAs = arr[np.char.find(arr[:, 0], 'A') == 0][:, 0]

print(f"Todas as empresas que começam com a letra A são: {arr_empresAs}")

arr_empresAs = np.char.upper(arr_empresAs)          # colocando todas as letras em forma maiuscula
arr_empresAs_ordenadas = arr_empresAs.sort()        # ordenando as empresas

print(f"Todas as empresas que começam com a letra A mostradas de forma ordenada são: {arr_empresAs}")

# EX3
# arr_USA = len(arr[np.char.find(arr[:, 3], 'United States') >= 0])   # quantidade de empresas fundadas nos USA
# arr_empresas = len(arr[1:, 3])                                      # total de empresas

# porcentagem de empresas fundadas nos USA
arr_empresas_USA = (len(arr[np.char.find(arr[:, 3], 'United States') >= 0]) / len(arr[1:, 3])) * 100

print(f"São {arr_empresas_USA}% do total de empresas deste dataset que são dos Estados Unidos")

# EX4
# Realizando o Slicing no dataset
arr_slicing = arr[1:, 0:3]

# Array das empresas fundadas após os anos 2000
arr_empresas_2000 = arr_slicing[arr_slicing[:, 2].astype(float) > 2000][:, 0]

print(f"As empresas fundadas após os anos 2000 são: {arr_empresas_2000}")

# EX5
# # anos em que as empresas foram fundadas
# arr_anos_fundadas = np.unique(arr[1:, 2])
# # relaciona o ano com a quantidade de empresas abertas
# arr_quantas_por_ano = np.column_stack(np.unique(arr[1:, 2], return_counts=True))
# # pega a quantidade máxima de empresas abertas em um ano
# arr_quantidade_max = (max(arr_quantas_por_ano[:, 1]))
# # Ano com a maior quantidade de empresas abertas
# arr_ano_com_mais_empresas = arr_quantas_por_ano[arr_quantas_por_ano[:, 1] == arr_quantidade_max][:, 0]

# Array que possui o ano em que mais empresas foram criadas
arr_ano = np.column_stack(np.unique(arr[1:, 2], return_counts=True))[np.column_stack(np.unique(arr[1:, 2], return_counts=True))[:, 1] == max(np.column_stack(np.unique(arr[1:, 2], return_counts=True))[:, 1])][:, 0]

print(f"O ano em que forma fundadas mais empresas foi em {arr_ano}")

