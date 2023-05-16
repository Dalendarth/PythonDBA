import numpy
numeros = 20
vetor = []

for i in range(numeros):
    valor = int(input('Digite um valor:'))
    vetor.append(valor)
    if valor % 2 == 0:
        print('Numero par!!!')
    else:
        print('Numero impar')