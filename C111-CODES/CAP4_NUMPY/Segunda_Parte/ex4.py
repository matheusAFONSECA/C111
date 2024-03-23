import ex2      # importando o código da questão 2 para usar a matriz gerada
import numpy as np          # importação da biblioteca NumPy

# Usando np.unique para obter os valores únicos e suas quantidades
val, quant = np.unique(ex2.mtz, return_counts=True)     # val -> array com os valores unicos
#                                                         quant -> quantidade de vezes que os números unicos apareceram

relacao = np.column_stack((val, quant))     # juntando os valores unicos e quantas vezes aparecerem em uma matriz
print(f"Números únicos(primeira coluna) e quantas vezes aparecem(segunda coluna) na matriz: \n{relacao}")
