import math

# Lê as coordenadas x e y
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

# Calcula a distância da origem
distancia = math.sqrt(x**2 + y**2)

# Imprime o resultado
print(f"A distância da origem é {distancia:.2f}.")