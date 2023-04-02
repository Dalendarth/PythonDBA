n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 > 0 and n2 > 0 and n3 > 0:
    raiz = (n1 * n2 * n3) ** (1/3)
    print(f"A média geométrica dos três números é: {raiz:.2f}")

    raiz = ((n1 + 2) * n2 + 3 * n3) / 6
    print(f"A média ponderada dos três números é: {raiz:.2f}")

    raiz = 3 / ((1/n1) + (1/n2) + (1/n3))
    print(f"A média harmônica dos três números é: {raiz:.2f}")

    raiz = (n1 + n2 + n3) / 3
    print(f"A média aritmética dos três números é: {raiz:.2f}")

elif n1 < 0 or n2 < 0 or n3 < 0:
    print("Pelo menos um número é negativo. Nenhum cálculo pode ser feito.")

else:
    print("Pelo menos um número é igual a zero. Nenhum cálculo pode ser feito.")


