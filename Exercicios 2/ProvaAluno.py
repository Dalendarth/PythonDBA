soma1 = 6 + 12
soma2 = 15 + 45
soma3 = 75 + 9
soma4 = 23 + 8
soma5 = 18 + 36
pontuacao = 0
geral = soma1 + soma2 + soma3 + soma4 + soma5
if soma1 == int(input("qual é o resultado de 6 + 12?")):
    print("correto")
    pontuacao += 1
else:
    resultado1 = 6 + 12
    print(f"errado o resultado é {resultado1}")
if soma2 == int(input("qual é o resultado de 15 + 45?")):
    pontuacao += 1
    print("correto")
else:
    resultado2 = 15 + 45
    print(f"errado o resultado é {resultado2}")
if soma3 == int(input("qual é o resultado de 75 + 9?")):
    pontuacao += 1
    print("correto")
else:
    resultado3 = 75 + 9
    print(f"errado o resultado é {resultado3}")
if soma4 == int(input("qual o resultado de 23 + 8?")):
    pontuacao += 1
    print("correto")
else:
    resultado4 = 23 + 8
    print(f"errado o resultado é {resultado4}")
if soma5 == int(input("Qual o resultado de 18 + 36?")):
    pontuacao += 1
    print("correto")
else:
    resultado5 = 15 + 36
    print(f"errado o resultado é {resultado5}")

print(f"valor total de todas as somas: {geral}, o aluno acertou: {pontuacao}")


