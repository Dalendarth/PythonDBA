notas_alunos = []
alunos_aprovados = 0

for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j + 1} do aluno {i + 1}: "))
        notas.append(nota)

    media = sum(notas) / len(notas)  # comando sum para somar elemento e len para obter tamanho da lista
    notas_alunos.append(media)  # adicionando a media ao vetor

    if media >= 7.0:
        alunos_aprovados += 1

print(f"O número de alunos com média maior ou igual a 7.0 é: {alunos_aprovados}")
