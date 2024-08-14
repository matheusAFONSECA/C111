import numpy as np          # importação da biblioteca NumPy

# NÚMEROS ALEATÓRIOS
# np.random.seed(10)                      # permite que a aleatoriedade seja a mesma para todas as máquinas -> como uma
# #                                       semente(seed) que todos plantaram juntos"""
# arr = np.random.randint(10, 20, 5)      # cria uma array com número aleatórios -> 5 números alatórios entre 10 e 20
#
# print(arr)

# ELEMENTOS ÚNICOS
# np.random.seed(5)
# arr = np.random.randint(0, 10, 15)
# print(arr)
# print(np.unique(arr))       # mostra elementos únicos
# print(set(arr))             # também mostra os elementos, mas em busca de maior desempenho, use o np.unique() mesmo

# OPERAÇÃO EM MATRIZES
# np.random.seed(10)
# mtz = np.random.randint(1, 11, 9).reshape(3, 3)     # matriz com números aleatórios
# print(mtz)
# # print(mtz.sum(axis=0))      # soma os valores das colunas
# # print(mtz.sum(axis=1))      # soma os valores das linhas
# # print(mtz.sum(axis=1)[0])   # mostra a soma dos valores da primeira linha da coluna
# # print(mtz.mean(axis=0)[1])
# # -> BROADCASTING
# # print(mtz*2)
# # -> CONDICIONAIS -> são como IFs dentro do argumento do proprio elemento
# #                 -> tudo que é feito em um IF pode ser feito em um condicional
# # arr = mtz[mtz%2==0]
# cond = mtz>mtz.mean()   # condição -> if
# arr = mtz[cond]         # aplica a condição na matriz
# print(cond)
# print(arr)

# NUMPY TAMBÉM PODE SER USADA EM TEXTOS
# TRABALHANDO COM TEXTOS
arr = np.array(['Giovanni', 'Isaque', 'Luíza', 'Raíssa'])
print(np.char.find(arr, 's'))       # retorna a posição onde encontrou a letra/combinação de letras(-1 não encontrou)
arr2 = arr[np.char.find(arr, 's')>=0]
print(arr2)
