import math

num = float(input("Digite um Numero qualquer: "))

if num < 0:
    print("Numero Invalido!")
else:
    log = math.log(num)  # nesse caso usei math.log funcao logaritmo da biblioteca math
    print(f"O logaritmo do numero digitado é: {log}")
