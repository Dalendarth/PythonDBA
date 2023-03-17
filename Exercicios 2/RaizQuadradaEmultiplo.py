import math

n1 = float(input("Digite um numero, seja positivo ou negativo:"))

if n1 >= 0:
    raizq = math.sqrt(n1)
    print(f"A raiz quadrada de {n1} é:{raizq}")
else:
    n2 = n1 ** 2
    print(f"O numero ao quadrado é: {n2}")