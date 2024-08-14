import numpy as np          # importação da biblioteca NumPy

np.random.seed(10)   # determinando a "seed" para a seleção dos n° aleatórios

mtz = np.random.randint(1, 51, 16)      # criando uma array com 16 valores aleatórios
mtz = mtz.reshape(4, 4)                 # criando matriz 4x4 com a array de 16 valores

print(f"Matriz 4x4: \n{mtz}")
