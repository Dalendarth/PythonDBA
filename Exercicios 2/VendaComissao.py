venda = float(input("Digite o valor da venda: "))

if venda >= 100000:
    comissao = venda * 16/100 + 700.00
    print(f"O valor da comissão é de: R$ {comissao:.2f}")
elif 80000 <= venda < 100000:
    comissao = venda * 14/100 + 650.00
    print(f"O valor da comissão é de: R$ {comissao:.2f}")
elif 60000 <= venda < 80000:
    comissao = venda * 14/100 + 600.00
    print(f"O valor da comissão é de: R$ {comissao:.2f}")
elif 40000 <= venda < 60000:
    comissao = venda * 14/100 + 550.00
    print(f"O valor da comissão é de: R$ {comissao:.2f}")
elif 20000 <= venda < 40000:
    comissao = venda * 14/100 + 500.00
    print(f"O valor da comissão é de: R$ {comissao:.2f}")
elif venda < 20000:
    comissao = venda * 14/100 + 400.00
    print(f"O valor da comissão é de: R$ {comissao:.2f}")