tamanho = 10

vet = []

for i in range(tamanho):  # para indice na faixa de tamanho:
    numero = int(input('Digite um numero inteiro: '))
    vet.append(numero)  # adiciona um novo valor a lista ou vetor

print('Os valores digitados são:')
for numero in vet:
    print(numero)
