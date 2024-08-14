import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('..\\space.csv', delimiter=';', dtype=str, encoding='utf-8')
arr = np.delete(arr, 0, axis=0)     # deletando o cabeçalho da array

# criando uma numpy array que vai correlacionar a empresa com a quantidade de missoes feitas
missoes_por_empresa = np.column_stack(np.unique(arr[:, 1], return_counts=True))

# mostrando a empresa e a quantidade de missões feitas
print("\n".join([f"Empresa: {empresa}, Quantidade de Missões: {missao}" for empresa, missao in missoes_por_empresa]))

