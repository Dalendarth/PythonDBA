num = []

for i in range(1, 11):
    numero = int(input('Digite um número: '))
    num.append(numero)  # armazena 10 numeros na variavel num
    if num <= [0]:  # ao dizer para a linha se for negativo, tenho que mostrar [] para dizer que é da lista
        print('Numero invalido')
        break

soma = sum(num)
media = soma / len(num) # comando len dá todos os numeros digitados para fazer a divisao pela soma
