import math

AlturaDegrau = float(input("Digite a altura dos degraus: "))
AlturaDestino = float(input("Digite a altura que deseja chegar: "))

total = AlturaDestino / AlturaDegrau
total = math.ceil(total)###ceil, usado para arredondar o resultado para cima, caso necessario

print(f"Voce tem, {total} degraus para chegar ao seu objetivo! ")
