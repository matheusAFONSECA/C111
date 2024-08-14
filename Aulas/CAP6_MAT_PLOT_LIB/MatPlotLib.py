import pandas as pd                 # importação da biblioteca pandas
import numpy as np                  # importação da biblioteca numpy
import matplotlib.pyplot as plt     # sub-biblioteca do matplotlib

# # PLOT SIMPLES
# x = np.array([1, 2, 3, 4])      # criando de uma array para ser usada no eixo x
# y = x*2                         # broadcasting do array para criar o eixo y
# y2 = x**2                       # broadcasting do array para criar o eixo y
# # etiquetando os eixos dos gráficos
# plt.xlabel('Valores de X')      # linhas
# plt.ylabel('Valores de Y')      # colunas
# # plotando o gráfico
# plt.plot(x, y, 'o--g', x, y2, 'b:o',
#          linewidth=3, markersize=20)       # fmt = [marker][line][color]
# plt.show()

# # SUBPLOTS
# x = np.array([1, 2, 3, 4])      # criando de uma array para ser usada no eixo x
# y = x*2                         # broadcasting do array para criar o eixo y
# y2 = x**2                       # broadcasting do array para criar o eixo y
# # Plot 1
# plt.subplot(1, 2, 1)
# plt.title('Linear')
# plt.xlabel('Valores de X')      # linhas
# plt.ylabel('Valores de Y')      # colunas
# plt.plot(x, y, 'x--r')
# # Plot 2
# plt.subplot(1, 2, 2)
# plt.title('Exponencial')
# plt.xlabel('Valores de X')      # linhas
# plt.ylabel('Valores de Y')      # colunas
# plt.plot(x, y2, 'o:g')
# # mostrando os graficos
# plt.show()

# SCATTER PLOT
df = pd.read_csv('paises.csv', delimiter=';')       # carregando um aquivo '.csv' com pandas
# seis maiores países
df2 = df.nlargest(6, 'Area (sq. mi.)')
# plotando o gráfico
plt.scatter(x=df2['Country'],
            y=df2['Area (sq. mi.)'],
            s=df2['GDP ($ per capita)']/50)
plt.show()
