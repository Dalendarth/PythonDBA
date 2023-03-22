import math

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o Segundo numero:"))
num3 = float(input("Digite o terceiro numero:"))

if num1 == num2 == num3:
    print("Triangulo Equilatero")
elif num1 == num2 or num2 == num3 or num3 == num1:
    print("Triangulo isosceles")
elif num1 != num2 and num2 != num3 and num3 != num1:
    print("Triangulo escaleno")
elif num1 + num2 > num3 and num2 + num3 > num1 and num3 + num1 > num2:
    print("Triangulo nao eh escaleno")
else:
    print("Numero Invalido")