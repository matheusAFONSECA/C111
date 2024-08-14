# COLEÇÕES

# LISTA

# guardando os elementos dentro de uma lista[]
nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
print(nomes)

# permite mais liberdade de trabalhar com os dados que a Tupla
# permite modificações -> MUTÁVEL

# ADD
nomes.append('Picolo')  # adiciona o elemento no final da lista

# UPDATE
nomes[0] = 'Bulma'

# DELETE
nomes.remove('Trunks')  # remoção por valor
del nomes[1]            # remoção por indice

# SELECT
print(nomes)
