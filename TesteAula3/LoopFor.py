'''
nome = 'guilherme'.lower()
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # tem que transformar em uma lista

# Exemplo de for 1 (iterando em uma string):
for letra in nome:  # para cada letra em nome
    print(letra)  # imprime letra

# Exemplo de for 2 (iterando sobre uma lista):
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range):

OBS: range (o valor final não é inclusive. porque a estrutura geralmente pode começar com 0)

for numero in range(1, 10):
    print(numero)

    nome = 'guilherme'.lower()
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # tem que transformar em uma lista

enumerate: vai colocar a primeira letra no indice 0, sempre partindo com o primeiro numero sendo 0
ou seja, ele atribui uma sequencia numerica para um indice, lembrando sempre partindo do 0

for i, v in enumerate(nome):    # i = indice, v = valor
    print(nome[i])
    ou
    for indice, letra in enumerate(nome):
    print(letra)
    Quando não precisamos de um valor, podemos descarta-lo usando o "_" como a seguir:
for _, letra in enumerate(nome): # descarta o indice e imprime a letra
    print(letra)

    nome = 'guilherme'.lower()
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # tem que transformar em uma lista

for valor in enumerate(nome): # essa linha é responsavel por mostrar o numero equivalente a letra da frase
    print(valor)

nome = 'guilherme'.lower()
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # tem que transformar em uma lista



qtd = int(input('Quuantas vezes esse loop deve rodar?'))
soma = 0
for n in range(1, qtd + 1): # quantidade + 1 para ir de 0 a 5
    print(f'Imprimindo {n}')

    qtd = int(input('Quuantas vezes esse loop deve rodar?'))
soma = 0
for n in range(1, qtd + 1):  # quantidade + 1 para ir de 0 a 5
    num = int(input(f'informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')  # essa linha está fora do bloco 'for'
O EXEMPLO ACIMA PEDE CONSECUTIVAMENTE A ENTRADA DO USUÁRIO, A ARMAZENA EM 'n' A ENTRADA
DO USUARIO, E REUTILIZA A QUANTIDADE DE ENTRADAS DE ACORDO COM O PRIMEIRO NUMERO QUE O USUARIO
DIGITOU, FAZENDO A SOMA DE TODAS AS ENTRADAS NO FINAL E IMPRIMINDO PORFIM O RESULTADO, ESSE É UM
EXEMPLO MAIS PRATICO NA MINHA OPNIÃO DE COMO APLICAR O LOOP FOR.

nome = 'guiherme'
for letra in nome:
    print(letra, end='')# imprimiu cada um dos caracteres sem pular as linhas
'''

nome = 'guiherme'
for letra in nome:
    print(letra, end='')# imprimiu cada um dos caracteres sem pular as linhas
