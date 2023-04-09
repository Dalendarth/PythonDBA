num = int(input('Digite um numero impar: '))

if num % 2 == 0:  # Se o resto da divisão for zero
    num += 1  # Adiciona 1 para tornar o numero impar
for i in range(num + 18, -2, -2):  # num + 10 adiciona os proximos 10 numeros da sequencia
    print(i)  # imprime o indice
