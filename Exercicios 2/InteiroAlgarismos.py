import math

num = int(input("Digite um numero inteiro: "))
soma = 0
if num < 0:
    print("Numero Invalido.")
    breakpoint()

for caractere in str(num):
    soma += int(caractere)
    print(soma)
