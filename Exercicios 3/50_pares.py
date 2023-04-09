soma = 0
for i in range(2, 101, 2):
    soma += i
    if i == 100:
        break

print("A soma dos primeiros 50 números pares é:", soma)