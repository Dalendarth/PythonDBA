import math

numero = int(input("Digite um Numero: "))

if 1000 <= numero <= 9999:
    #imprimindo um digito por linha
    print(numero // 1000)
    print(numero // 100 % 10)
    print(numero // 10 % 10)
    print(numero % 10)
else:
    print("O numero digitado não é valido. ")
