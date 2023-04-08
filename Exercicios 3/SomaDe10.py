print("Digite 10 valores diferentes:")
valores = []
for i in range(10):  # i = indice
    valor = int(input(f"Digite o valor {i+1}: "))
    valores.append(valor)   # Lista vazia para armazenar valores

# uso sum para realizar a soma
soma = sum(valores)

# Exibe o resultado da soma na tela
print(f"A soma dos valores é: {soma}")
