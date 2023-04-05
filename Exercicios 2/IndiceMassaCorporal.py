imc = float(input('Digite a massa corporal equivalente:'))

if imc <= 18.5:
    print('Abaixo do peso')
elif 18.6 < imc < 24.9:
    print('Saudavel')
elif 25.0 < imc < 29.9:
    print('Peso em excesso')
elif 30.0 < imc < 34.9:
    print('Obesidade Grau 1')
elif 35.0 < imc < 39.9:
    print('Obesidade Grau 2 (Severa)')
elif imc >= 40:
    print('Obesidade Grau 3 (Mórbida)')
else:
    inv = 0 >= imc > 300
    print(f'Enstrada invalida{inv}')

