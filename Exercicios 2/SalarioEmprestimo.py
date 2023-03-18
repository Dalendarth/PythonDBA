salario = float(input("Digite o valor do salário: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

limitePrestacao = salario * 0.2  # 20% do salário

if prestacao > limitePrestacao:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")