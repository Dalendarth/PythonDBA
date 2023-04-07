'''
Ranges

- precisa-se conhecer o loop for para para fazer uso dos ranges
- precisa-se conhecer mais o range, para trabalhar melhor o loop for
no caso acima, um depende do outro

de forma geral, ranges são utilizados para gerar sequencias numericas não de forma
aleatória, nas sim de maneira especificada.

formas gerais por exemplo:
range (valor_de_parada)

OBS: valor_de_parada não inclusive (inicia-se com o valor 0, e realiza o passo de 1 em 1)

#    exemplo 1:
for num in range(11):
    print(num)

#   exemplo 2:
for num in range(1, 11):
    print(num)

# exemplo 3:
for num in range(1, 10, 2): # o ultimo numero funciona como um delimitador de amostragem entre 2 e dois numeros
    print(num)

#exemplo 4:
for num in range(10, 0, -1):    # com o operador aritmetico "-", no ultimo numero, faz listagem decrescente.
print(num)
'''

for num in range(10, 0, -1):    # com o operador aritmetico "-", no ultimo numero, faz listagem decrescente.
    print(num)