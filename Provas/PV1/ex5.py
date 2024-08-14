import numpy as np      # importação da biblioteca de Numpy

# carregando o arquivo .csv para uma numpy array
arr = np.loadtxt('brands.csv', delimiter=';', dtype=str, encoding='utf-8')

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
