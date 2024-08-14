# criando a lista dos cinco classificados do mundial de futebol
lista = ['Barcelona', 'Flamengo', 'Real Madrid', 'Chelsea', 'Palmeiras']

# A) mostrando os três primeiros colocados:
print(lista[:3])

# B) Os últimos dois colocados:
print(lista[-2:])

# C) Lista dos clubes em ordem alfabética
lista_original = lista.copy()   # copiando o conteudo da lista original para responder a proxima questão
lista.sort()
print(lista)

# D) Posição em que o Barcelona está
print(lista_original.index('Barcelona'))
