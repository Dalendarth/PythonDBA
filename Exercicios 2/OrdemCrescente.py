n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terceiro numero:"))

if n1 > n2 > n3:
    print(f"a ordem crescente é:{n1}, {n2} e {n3} ")
elif n1 < n2 <n3:
    print(f"a ordem crescente é:{n1}, {n2} e {n3} ")
elif n2 > n1 < n3:
    print(f"a ordem crescente é: {n2}, {n1}, {n3}")
elif n3 > n2 < n1:
    print(f"a ordem crescente é:{n3}, {n2} e {n1} ")
else:
    print("numero invalido")