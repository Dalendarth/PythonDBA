nota = float(input("Digite a nota do aluno:"))
faltas = int(input("Digite o numero de faltas do aluno:"))

if nota <= 10 and faltas <= 20:
    print("O conceito final é A")
else:
    print("O conceito Final é B")
