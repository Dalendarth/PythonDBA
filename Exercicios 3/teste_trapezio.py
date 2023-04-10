import math
b1 = float(input('Digite a area 1: '))
b2 = float(input('Digite a area 2: '))
alt = float(input('Digite a altura:'))

area = (b1 + b2) * math.sqrt(alt)

print(f'Area do trapezio é de: {area}')

if b1 <=0 and b2 <= 0 and alt <=0:
    print('Numero invalido!')