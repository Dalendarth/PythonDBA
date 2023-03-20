

bMaior = float(input("Digite o numero da base Maior:"))
bMenor = float(input("Digite o numero da base Menor:"))
alt = float(input("Digite a altura"))
if bMaior >= 0 and bMenor >= 0:
    Area = (bMaior + bMenor) * alt / 2
    print(f"A area do Trapezio é de: {Area}")
else:
    print("Numero Invalido")

