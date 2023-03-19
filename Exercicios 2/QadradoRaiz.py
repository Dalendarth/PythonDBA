import math

n1 = float(input("Digite um Numero: "))

if n1 >= 0:
    quad = n1 ** 2
    raizq = math.sqrt(n1)
    print(f"O {n1} elevado ao quadrado fica {quad} e a raiz de {n1} é de {raizq} ")
else:
    print("Numero Invalido")
