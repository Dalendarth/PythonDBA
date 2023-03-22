import math

num = int(input("Digite um numero"))

if num % 3 == 0:
    print("Numero é divisivel por 3")
elif num % 5 == 0:
    print("Numero é divisivel por 5")
else:
    print("Numero não é divisivel por 3 nem por 5")