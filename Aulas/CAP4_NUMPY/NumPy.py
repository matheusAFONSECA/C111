import numpy as np          # importação da biblioteca NumPy

# Criando um NumPy Array(Termo Informal) - Ndarray(Termo Técnico)
# Uma Dimensão - 1D
arr = np.array([1, 2, 3, 4])
print(arr)              # printando o valor do NumPy Array
print(type(arr))        # mostrando o tipo da variável
# Uma Dimensão - 2D
mtz = np.array([[1, 2], [3, 4]])
print(mtz)              # printando o valor do NumPy Array
print(type(mtz))        # mostrando o tipo da variável

# NumPy Array só pode guardar dados do mesmo tipo

# Estruturando NumPy Arrays Automaticamente
mtz = np.ones(9)           # criando um vetor só com o número 1 - Argumento é a quantidade de 1
print(mtz)

mtz = np.ones(9).reshape(3, 3)      # remodelando o vetor para se torna uma matriz 3x3 - usando o método reshape
#                                    esse método exige que as dimensões da matriz esteja compativel em tamanho
#                                    com o vetor
print(mtz)

# Zeros
# Arange
mtz = np.arange(10, 20, 2)          # cria uma array de numéros entre 10 e 20 que pula de dois em dois, exclusive 20
print(mtz)

# Operações Elemento a Elemento
arr1 = np.arange(10, 20, 1)
arr2 = np.arange(30, 40, 1)

print(arr1)
print(arr2)
print(arr1 + arr2)      # soma os elementos em cada posição e salva o resultado na posição relacionada
print(np.concatenate([arr1, arr2]))       # concatenar os elementos de duas arrays

# Propriedades de um NumPy Array
print(arr1.size)    # tamanho
print(arr1.ndim)    # quantidade das dimensões
print(arr1.shape)   # formato
