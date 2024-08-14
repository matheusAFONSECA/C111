import ex2      # importando o código da questão 2 para usar a matriz gerada

colunas = ex2.mtz.sum(axis=0)       # soma os valores das colunas
linhas = ex2.mtz.sum(axis=1)        # soma os valores das linhas
# print(f"Soma dos valores das colunas \n{colunas}")
# print(f"Soma dos valores das linhas \n{linhas}")

colunas = colunas / 4               # faz a média dos valores de cada coluna
linhas = linhas / 4                 # faz a média dos valores de cada linha
print(f"Média dos valores das colunas \n{colunas}")
print(f"Média dos valores das linhas \n{linhas}")

maior_coluna = max(colunas)      # pega o maior valor das médias das colunas
maior_linha = max(linhas)        # pega o maior valor das médias das linhas
print(f"Maior valor das médias das colunas é: {maior_coluna} ")
print(f"Maior valor das médias das linhas é: {maior_linha} ")



