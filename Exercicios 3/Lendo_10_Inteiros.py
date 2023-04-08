num = []

for i in range(1, 11):
    numero = int(input('Digite um número: '))
    num.append(numero) # armazena 10 numeros na variavel num

soma = sum(num)
media = soma / len(num)

print(f'A média dos números é: {media}')


'''
# Exemplo usando len
lista = [1, 2, 3, 4, 5]
tamanho = len(lista)
print("O tamanho da lista é:", tamanho)

# Exemplo usando sum
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
print("A soma dos números é:", soma)
'''

