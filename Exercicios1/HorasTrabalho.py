import math

horas = float(input("Digite as horas trabalhadas: "))
valor = 5.51
bruto = horas * valor
pagamento = bruto + 0.10

print(f"O valor total a ser pago é de: {pagamento:.2f}")
