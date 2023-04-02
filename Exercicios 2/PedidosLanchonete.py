pedido = int(input(f"Digite o código do produto: "))
CodProduto = [100, 101, 102, 103, 104, 105, 106]
quant = int(input("Digite a quantidade:"))

if pedido == 100:
    print("Produto escolhido: Cachorro quente")
    total = 1.20 * quant
    print(f"Total a ser pago é de {total}")
elif pedido == 101:
    print("Produto escolhido: Bauru Simples")
    total = 1.30 * quant
    print(f"Total a ser pago é de {total}")
elif pedido == 102:
    print("Produto escolhido: bauru com ovo")
    total = 1.50 * quant
    print(f"Total a ser pago é de {total}")
elif pedido == 103:
    print("Produto escolhido: Hamburguer")
    total = 1.20 * quant
    print(f"Total a ser pago é de {total}")
elif pedido == 104:
    print("Pruduto escolhido: CheeseBurguer")
    total = 1.70 * quant
    print(f"Total a ser pago é de {total}")
elif pedido == 105:
    print("Produto escolhido: Suco")
    total = 2.20 * quant
    print(f"Total a ser pago é de {total}")
elif pedido == 106:
    print("Produto escolhido: Refrigerante")
    total = 1.00 * quant
    print(f"Total a ser pago é de {total}")
else:
    print("Entrada invalida")