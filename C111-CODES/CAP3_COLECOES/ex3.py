# entrando com o nome e media do aluno
nome = input("Nome: ")
media = input("Média: ")

# criando o dicionário com esses valores
aluno = {"Nome": nome, "Média": media}

# determinando se o aluno foi aprovado ou reprovado
if int(media) >= 60:
    situacao = "AP"
else:
    situacao = "RP"

# adicionando a situação do aluno ao dicionario
aluno['Situação'] = situacao

# mostrando o conteudo do dicionário
print(aluno)
