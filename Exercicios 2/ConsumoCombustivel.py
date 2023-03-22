
distancia = float(input("Digite a Distancia percorrida em Km: "))
litros = float(input("Digite quantos Litros foram consumidos: "))

ConsumoTotal = distancia / litros
if distancia and litros < 0:
    print("Numeros inválidos")

if ConsumoTotal <= 8:
    print("O Carro não é econômico")
elif ConsumoTotal > 8 and ConsumoTotal <= 14:  # OBS: senãoSe 8 entre 14
    print("Econômico")
elif ConsumoTotal > 12:
    print("Super Economico")

