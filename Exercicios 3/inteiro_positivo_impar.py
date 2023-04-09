n = int(input('Digite um numero impar:'))
if n % 2 == 0:
    n += 1
for i in range(1, n, 3):    # De 1 até n pulando 3 numeros
    print(i)


