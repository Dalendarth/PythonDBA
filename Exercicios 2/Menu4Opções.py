print("Escolha uma das seguintes operações: Soma, Divisão, Subtração e Multiplicação:")

print("Soma para somar")
print("Divisão para dividir")
print("Subtração para subtrair")
print("Multiplicação para multiplicar")

operacao = input("Escolha a operação desejada: ").lower()

if operacao == "soma":
    num1 = float(input("Digite o Primeiro Numero: "))
    num2 = float(input("Digite o Segundo Numero: "))
    res = num1 + num2
    print(f"O Resultado da Soma é de: {res}")
elif operacao == "divisão":
    num1 = float(input("Digite o Primeiro Numero: "))
    num2 = float(input("Digite o Segundo Numero: "))
    res = num1 / num2
    print(f"O Resultado da Divisão é de: {res}")
elif operacao == "subtração":
    num1 = float(input("Digite o Primeiro Numero: "))
    num2 = float(input("Digite o Segundo Numero: "))
    res = num1 - num2
    print(f"O Resultado da Subtração é de: {res}")
elif operacao == "multiplicação":
    num1 = float(input("Digite o Primeiro Numero: "))
    num2 = float(input("Digite o Segundo Numero: "))
    res = num1 * num2
    print(f"O Resultado da Multiplicação é de: {res}")
else:
    print("Operação inválida")
