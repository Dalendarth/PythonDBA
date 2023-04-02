altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

if altura < 1.20 and peso <= 60:
    print("Classificação A")
elif (1.20 < altura < 1.70) and (60 < peso < 90):
    print("Classificação D")
elif altura > 1.70 and peso > 90:
    print("Classificação G")
else:
    print("Entrada Invalida")
