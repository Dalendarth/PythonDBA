numero_digitado = int(input("Digite um número em minutos: "))
horas = numero_digitado // 60
minutos = numero_digitado % 60  # operador mod usa de resto para separar hora de minuto
print(f"{numero_digitado} minutos equivalem a {horas} horas e {minutos} minutos")


if 1 < horas < 2:
    print("Valor do estacionamento: 1.00")
elif 3 < horas < 4:
    print("Valor do estacionamento: 1.40")
elif horas >= 5:
    print("Valor do estacionamento: 2.00")
else:
    print("Entrada invalida")