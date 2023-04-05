import math
num = float(input("Digite um número real: "))

if num >= 0:
    pos = True
else:
    pos = False

if pos:
    raizq = math.sqrt(num)
    print(f"A raiz quadrada de", num, "é:", raizq)
else:
    quadrado = num ** 2
    print("O quadrado de", num, "é:", quadrado)