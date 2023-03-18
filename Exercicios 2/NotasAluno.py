n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

if n1 > 0 and n2 > 0:
    print(f"As notas digitadas foram: {n1} e {n2}, correto?")
    while True:
        s = input("Deseja calcular a média? (S/N) ")
        if s.upper() == "S":
            m = (n1 + n2) / 2
            print(f"A média das notas é: {m}")
            break
        elif s.upper() == "N":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Digite S para calcular a média ou N para encerrar o programa.")
else:
    print("Nota inválida. Reiniciando questionário")
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    if n1 > 0 and n2 > 0:
        print(f"As notas digitadas foram: {n1} e {n2}")
        while True:
            s = input("Deseja calcular a média? (S/N) ")
            if s.upper() == "S":
                m = (n1 + n2) / 2
                print(f"A média das notas é: {m}")
                break
            elif s.upper() == "N":
                print("Encerrando programa...")
                break
            else:
                print("Opção inválida. Digite S para calcular a média ou N para encerrar o programa.")

