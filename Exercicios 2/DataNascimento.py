dia = int(input('Digite o dia de nascimento: '))
mes = int(input('Digite o mes de nascimento: '))

if mes == 2 and dia > 28:
    print('Dia de nascimento inválido para o mês de fevereiro')
elif mes in [4, 6, 9, 11] and dia > 30:
    print('Dia de nascimento inválido para o mês informado')
elif dia > 31:
    print('Dia de nascimento inválido')
else:
    print('Dia de nascimento válido')
