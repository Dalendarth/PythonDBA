import math

valor = float(input("Digite o valor original: "))
desconto = valor * 0.10
valor_com_desconto = valor - desconto
comissao = valor_com_desconto * 0.05
valor_com_comissao = valor_com_desconto + comissao
valor_parcela = valor_com_comissao / 3
print(f"Valor original: {valor:.2f}")
print(f"Valor com desconto de 10%: {valor_com_desconto:.2f}")
print(f"Valor da parcela: {valor_parcela:.2f}")
print(f"Valor com comissão de 5%: {str(valor_com_comissao):.2f}")