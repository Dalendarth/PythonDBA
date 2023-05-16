totais = 4  # quantidade de entradas que o usuario dará
notas = []  # entrada de notas
soma = 0  # soma iniciada em zero por padrão

for i in range(totais):
    valor = float(input('Digite uma nota: '))
    notas.append(valor)  # adicionando notas com comando append a lista
    soma += valor   # atribuindo ou somando os valores digitados

media = soma / totais   # calculando a media
print(f'A média das quatro notas digitadas é de: {media}') 
