# Lê um número inteiro de segundos
total_segundos = int(input("Digite um número de segundos: "))

# Calcula horas, minutos e segundos
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = (total_segundos % 3600) % 60

# Imprime o resultado formatado
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")