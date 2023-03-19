import math

num = float(input("Digite um número: "))

if num < 0:
    print("Número inválido!")
else:
    log = math.log(num, 10)
    print(f"O logaritmo na base 10 do número digitado é: {log}")