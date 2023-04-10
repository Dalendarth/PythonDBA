ini = input('Olá, deseja iniciar a emulação de uma maquina S/N?').lower()

if ini == 's':
    print('Maquina em desenvolvimento. Selecione uma das funções a seguir:')
    var = input('Calculadora, Informações basicas, Finalizar:   ').lower()
    if var == 'calculadora':
        print('Qual operação deseja calcular?')
        op = input('Soma, Divisão, Subtração ou Multiplicação?').lower()
        if op == 'soma':
            n1 = float(input('Digite o primeiro Numero: '))
            n2 = float(input('Digite o segundo Numero: '))
            res = n1 + n2
            print(f'Resultado da soma é de: {res}, finalizando programa...')
        elif op == 'divisao' or op == 'divisão':
            op2 = input('O usuário quer solicitar uma divisão Normal ou Inteira?').lower()
            if op2 == 'normal':
                print('Divisão escolhida: Normal')
                n1 = float(input('Digite o primeiro numero: '))
                n2 = float(input('Digite o segundo numero: '))
                res = n1 / n2
                print(f'O resultado da divisão normal é de: {res}')
            elif op2 == 'inteira':
                print('Divisão escolhida: Inteira')
                n1 = float(input('Digite o primeiro numero: '))
                n2 = float(input('Digite o segundo numero: '))
                res = n1 // n2
                print(f'O resultado da divisão inteira é de: {res}')
            elif op == 'subtração' or op == 'subtracao':
                print('Escolhido: Subtração')
                n1 = float(input('Digite o primeiro numero: '))
                n2 = float(input('Digite o segundo numero: '))
                res = n1 - n2
                print(f'O Resultado da subtração é de: {res}')
            elif op == 'Multiplicação' or op == 'multiplicacao':
                print('Escolhido: Multiplicação')
                n1 = float(input('Digite o primeiro numero: '))
                n2 = float(input('Digite o segundo numero: '))
                res = n1 * n2
                print(f'O resultado da multiplicação é de: {res}')
    elif var == 'Informações Basicas' or var == 'informacoes basicas':
        print('Um software simples para testar estrutura condicional, variaveis para implementação de loops :D')
    elif var == 'Finalizar':
        print('Finalizando, isso é tudo por enquanto ^^')
else:
    print('Entrada Invalida!')
