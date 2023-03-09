real = float(input("Informe o valor em reais: "))
cotacao = float(input("Informe a cotação do dólar: ").replace(',', '.'))###para possibilitar virgula na casa decimal

ValorEmDolar = real / cotacao


print("Valor em dólar:", ValorEmDolar)