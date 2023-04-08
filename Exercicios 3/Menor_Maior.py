num = []
menor = float('inf')  # inicializa a variável com um valor que representa o infinito positivo
maior = float('-inf')  # inicializa a variável com um valor que representa o infinito negativo

for i in range(1, 11):
    numero = int(input('Digite um número: '))
    num.append(numero)  # vai pedir para repetir a linha de cima 10x
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')
