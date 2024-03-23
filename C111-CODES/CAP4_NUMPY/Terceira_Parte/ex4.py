import numpy as np          # importação da biblioteca NumPy

# carregando o arquivo '.csv' em uma array do numpy
arr = np.loadtxt('..\\space.csv', delimiter=';', dtype=str, encoding='utf-8')
arr = np.delete(arr, 0, axis=0)     # deletando o cabeçalho da array

# O comando abaixo entrega direto a resposta, mas ficou muito poluido de entender, por isso separei as missões da SpaceX
# e depois filtrei as viagens mais caras
# SpaceX = arr[np.char.find(arr[:, 1], 'SpaceX') >= 0][arr[np.char.find(arr[:, 1], 'SpaceX') >= 0][:, 6] == max(arr[np.char.find(arr[:, 1], 'SpaceX') >= 0][:, 6])]

# Pega todas as missões da SpaceX
missoes_SpaceX = arr[np.char.find(arr[:, 1], 'SpaceX') >= 0]

# dentre as missões da SpaceX retorna as missões mais caras
SpaceX_mais_cara = missoes_SpaceX[missoes_SpaceX[:, 6] == max(missoes_SpaceX[:, 6])]

print(f"A(s) missão(ões) da SpaceX mais cara(s): \n{SpaceX_mais_cara}")
