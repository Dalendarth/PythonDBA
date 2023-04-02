preco = float(input("Digite um preço: "))

if preco <= 50:
    percentual = 5
elif preco > 50 and preco <= 100:
    percentual = 10
else:
    percentual = 15

preco_com_aumento = preco * (1 + percentual/100)

print(f"O preço com aumento é R$ {preco_com_aumento:.2f}")



