num = int(input('Digite um numero inteiro'))
if num < 0:
    print('Numero invalido')
else:
    soma = 0
    for i in range(1, num + 1):
        soma += i

    print(f'a soma dos naturais de {num} é {soma}! ')
