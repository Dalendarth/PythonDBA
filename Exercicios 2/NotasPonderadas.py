num1 = float(input("Digite a nota de Trabalho em Laboratorio"))
num2 = float(input("Digite a Avaliação Semestral"))
num3 = float(input("Digite Nota do Exame Final"))
lab = 2
sem = 3
ef = 5
mPonderada = (num1 * lab + num2 * sem + num3 * ef) / (lab + sem + ef)

if mPonderada <= 2.9:
    print(f"Aluno Reprovado, Nota: {mPonderada}")
elif 3 >= mPonderada <= 4.9: # SenãoSe 3 for maior ou igual a variavel e 4.9 for menor ou igual a variavel
    print(f"Aluno De Recuperação, Nota: {mPonderada}")
else:
    print(f"Aluno Aprovado, Nota:{mPonderada}")