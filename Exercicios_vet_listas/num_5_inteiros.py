'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.'''
vetor = []

# Ler os números do usuário e adicionar ao vetor
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

# Calcular a soma dos números no vetor
soma = sum(vetor)

# Calcular a multiplicação dos números no vetor
multiplicacao = 1
for numero in vetor:
    multiplicacao *= numero

# Exibir os resultados
print("Números:", vetor)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)
