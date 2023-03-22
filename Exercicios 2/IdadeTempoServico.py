

idade = int(input("Digite sua idade:"))
Tservico = int(input("Digite o tempo de serviço:"))

if idade >= 65:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")
    if Tservico >= 30:
        print("Pode se aposentar")
    else:
        print("Não pode se aposentar")
        if idade >= 60 and Tservico >= 25:
            print("Pode se aposentar")
        else:
            print("Não pode se aposentar")
