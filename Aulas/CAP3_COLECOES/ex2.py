# defindo as lojas e modelos que cada uma vende
loja1 = {'Samsung - S24', 'Apple - iphone 14', 'Apple - iphone 15', 'Motorola - g73'}
loja2 = {'Samsung - S24', 'Apple - iphone 14', 'Motorola - g53', 'Samsung - S23'}

# Mostrando os modelos que cada uma das lojas vendem
print("LOJA 1: ", loja1)
print("LOJA 2: ", loja2)

# Mostrando quantos modelos são possiveis serem comprados
loja = loja1 | loja2
print("São ", len(loja), " modelos disponíveis")
print("Modelos disponíveis: ", loja)

# Modelos disponíveis em ambas as lojas
print("Ambas as lojas disponibilizam os modelos: ", loja1 & loja2)
