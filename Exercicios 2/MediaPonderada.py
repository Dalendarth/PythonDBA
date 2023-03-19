
num1 = float(input("Digite a primeira nota"))
num2 = float(input("Digite a segunda nota"))
num3 = float(input("Digite a terceira nota"))
p1 = 1
p2 = 2
mPonderada = (num1 * p1 + num2 * p2 + num3) / (p1 + p2 +1)

if mPonderada >= 60:
    print(f"Aluno aprovado: {mPonderada}")
else:
    print("Aluno Reprovado")