quantidade = int(input('Digite a quantidade de números que deseja digitar: '))

contagem = {}
maior_repetido = None
maior_contagem = 0

for i in range(quantidade):
    numero = int(input(f'Digite o {i+1}° número: '))
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

    if contagem[numero] > maior_contagem:
        maior_repetido = numero
        maior_contagem = contagem[numero]

if maior_repetido is not None:
    print(f'O maior número repetido é {maior_repetido}, que foi digitado {maior_contagem} vezes.')
else:
    print('Nenhum número foi repetido.')

