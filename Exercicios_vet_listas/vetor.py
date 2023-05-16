# Definindo o tamanho do vetor
tamanho = 5

# Criando um vetor vazio
vetor = []

# Lendo os valores do vetor
for i in range(tamanho):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

# Mostrando os números do vetor
print("Os números digitados são:")
for numero in vetor:
    print(numero)
