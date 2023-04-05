valor = float(input('Digite o valor do salario do funcionário: '))
tempo_servico = int(input('Digite o numero de anos de trabalho na empresa: '))

if valor <= 500.00 and tempo_servico < 1:
    aumento = valor * 25 / 100
    print(f'Salario com reajuste é de: {aumento}, sem bonus.')
elif valor <= 1000.00 and tempo_servico in range (1, 3):# de um a tres anos de trabalho
    aumento = valor * 20 / 100 + 100
    print(f'Salario com reajuste é de: {aumento} com bonus de 100.00')
elif valor <= 1500.00 and tempo_servico in range (4, 6):
    aumento = valor * 15/100 + 200
    print(f'Salario com reajuste é de: {aumento} com bonus de 200.00')
elif valor <= 2000.00 and tempo_servico in range (7, 10):
    aumento = valor * 10 / 100 + 300
    print(f'Salario com reajuste é de: {aumento} com bonus de 300.00')
elif valor >= 2000.00 and tempo_servico > 10:
    aumento = valor + 500
    print(f'Salario sem reajuste, com adicional de 500.00')
else:
    print('Valor Invalido')


