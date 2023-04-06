din = float(input('Digite o valor recebido: '))

if din <= 0:
    print('Valor Invalido')
elif din >= 1:
    quant_prod = int(input('Digite a quantidade do produto escolhido: '))
    valor = float(input('Digite o valor do produto: '))
    total = quant_prod * valor
    print(f'O valor total do produto é de: {total}:.2f')
    if din < total:
        print('Quantidade recebida é inválida')
    elif din >= total:
        troco = din - total
        print(f'O troco é de: {troco}:.2f')
        if din == total:
            print('Não há troco a receber, o valor está certo. Muito Obrigado!')
        else:
            print('Valor não reconhecido.')

