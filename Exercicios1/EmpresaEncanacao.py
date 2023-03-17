import math

dias = float(input("Digite os dias trabalhados: "))
ValorUnitario = 30.00
ValorTotalDias = dias * ValorUnitario
desconto = 0.08 * ValorTotalDias
liquido = ValorTotalDias - desconto
print(f"Valor total a ser pago pelos {dias} dias trabalhados: R$ {ValorTotalDias:.2f}")
print(f"Desconto a ser aplicado: R$ {desconto:.2f}")
print(f"Valor líquido a ser pago: R$ {liquido:.2f}")


