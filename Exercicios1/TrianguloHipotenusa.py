import math

a = float(input("Digite o primeiro cateto: "))
b = float(input("Digite o segundo cateto: "))

hipotenusa = math.sqrt(a ** 2 + b ** 2)### math.sqrt (raiz quadrada) de A ao quadrado + B ao quadrado

print(f"O valor da hipotenusa é de: {hipotenusa}")
