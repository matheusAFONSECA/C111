import pandas as pd
import numpy as np

# SERIES (1D)
dic = {'a': 10,
       'b': 20,
       'c': 30}       # criando um dicionário -> estrutura "chave": valor

"""s = pd.Series(dic)
print(s)
print(type(s))      # ver o tipo da variável"""

s1 = pd.Series(dic)
s2 = pd.Series(data=[20, 30, 40],
               index=['a', 'b', 'd'])

"""print(s1 + s2)
print(s1.add(s2, fill_value=0))     # aquilo que é vazio é tratado como 0
print(s1['b'])
print(s1[['b', 'c']])"""

# print(s1[s1 > s1.mean()])       # usando um condicional que retorna o valor maior que a média dos valores contidos em s1

# DATAFRAMES (2D)
"""df = pd.DataFrame(
    index=['A', 'B', 'C', 'D'],
    columns=['X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [4, 3])
)

print(df)

# slicing com loc
print(f"slicing com loc:\n{df.loc[['B', 'C'], ['X', 'Y', 'Z']]}")
# slicing com iloc
print(f"slicing com iloc:\n{df.iloc[1:3, :]}")"""

csv = pd.read_csv('paises.csv', delimiter=';')
print(csv)
print(csv['Country'])
print(csv.head(5))
print(csv.tail(2))
