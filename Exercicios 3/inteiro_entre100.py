numero = int(input("Digite um número inteiro entre 100 e 999: "))

for i in range(3):
    digito = numero % 10
    print(digito)
    numero = numero // 10
