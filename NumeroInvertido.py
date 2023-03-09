# Lendo um número inteiro positivo de três dígitos
numero = int(input("Digite um número inteiro positivo de três dígitos: "))

# Verificando se o número é válido
if 100 <= numero <= 999:
    # Gerando o número formado pelos dígitos invertidos
    NumeroReverso = (numero % 10) * 100 + (numero // 10 % 10) * 10 + (numero // 100)
    print("O número formado pelos dígitos invertidos é:", NumeroReverso)
else:
    print("O número digitado não é válido.")