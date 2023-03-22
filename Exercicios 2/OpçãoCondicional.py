print("Escolha uma das opções:")

print("1 - Soma de 2 numeros.")
print("2 - Diferença entre 2 numeros (maior pelo menor)")
print("3 - Produto entre 2 numeros")
print("4 - Divisão entre 2 numeros (Denominador não pode ser 0)")
operacao = input("Digite o numero da operação desejada:")

if operacao == "1":
    print("Operação escolhida: Soma")
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
    res = num1 + num2
    print(f"O resultado da soma é: {res}")
elif operacao == "2":
    print("Operação escolhida: Diferença entre dois Numeros, maior pelo menor.")
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
    if num1 > num2:
        print(f"O maior entre os dois numeros é: {num1}")
    else:
        print(f"O maior entre os dois numeros é: {num2}")
elif operacao == "3":
    print("Operação escolhida: Produto entre dois numeros")
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
    res = num1 * num2
    print(f"O resultado do Produto é: {res}")
elif operacao == "4":
    print("Operação escolhida: Divisão entre dois numeros (Denominador não pode ser menor ou igual a 0)")
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))
    res = num1 / num2
    print(f"O resultado da Divisão é: {res}")
    if num1 < 0 or num2 < 0:
        print("Denominador não pode ser 0 ou menor que 0")
else:
    print("Numero Invalido!")
