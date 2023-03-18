import math

n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))

if n1 > n2:
    sub = n1 - n2
    print(f"O Numero maior é {n1}, tem a diferença de {sub}, do segundo numero.")
else:
    sub = n2 - n1
    print(f"O numero maior é {n2}, tem a diferença de {sub}, do primeiro numero.")