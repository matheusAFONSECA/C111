# COLEÇÕES

# DICIONÁRIOS

# guardando os elementos dentro de um dicionário{chave: valor}
pessoa = {
    'nome': 'Goku',
    'idade': 42
}
print(pessoa)

# Mutável e com a possibilidade de ser mais específico nos comandos

# ADD
pessoa['sexo'] = 'M'

# DELETE
del pessoa['idade']

# UPDATE
pessoa['nome'] = 'Gohan'

pessoa2 = {
    'nome': 'Bulma',
    'idade': 32
}

print(pessoa)
print(pessoa2)

# usa chaves que podem variar conforme desejamos ter um valor relacionado
# usado em arquivos '.json'

# Agora veremos o uso de conceito de coleção dentro de uma coleção
pessoas = [pessoa, pessoa2]     # lista de dicionários
print(pessoas)                  # mostrando os dados dentro de uma lista
print(pessoas[1])                  # mostrando os dados dentro de uma lista
print(pessoas[0]['nome'])       # mostrando um dado específio de uma posição na lista e por meio da chave do dicionário
