import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('..\\space.csv', delimiter=';', dtype=str, encoding='utf-8')

contagem_total = len(arr) - 1                                          # quantidade total de missões
#                                                                        coloquei o -1 para não contar o cabeçalho
contagem_sucesso = len(arr[np.char.find(arr, 'Success') >= 0])         # quantidade de missões de sucesso
print(f"Quantidade total de missões: {contagem_total}")
print(f"Quantidade de missões com sucesso: {contagem_sucesso}")

# mostra a porcentagem de missões que foram um sucesso
print(f"Porcentagem de sucesso: {((contagem_sucesso/contagem_total)*100):.2f}%")
