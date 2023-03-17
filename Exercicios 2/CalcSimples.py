import math

n1 = int(input("Digite primeiro numero inteiro para a soma: "))
n2 = int(input("Digite o segundo numero inteiro para a soma: "))

soma = n1 + n2

s1 = int(input("Digite primeiro numero inteiro para a subtração: "))
s2 = int(input("Digite o segundo numero inteiro para a subtração: "))

sub = s1 - s2

d1 = float(input("Digite o primeiro numero real para divisão:"))
d2 = float(input("Digite o segundo numero real para a divisão:"))

divisao = d1/d2

m1 = int(input("Digite o primeiro numero da multiplicacao:"))
m2 = int(input("Digite o segundo numero da multiplicacao:"))

multiplicacao = m1 * m2

r = float(input("Digite um numero real para raiz:"))

raiz = math.sqrt(r)

print(f"Os resultados são, soma: {soma},subtração:{sub} divisao:{divisao},multiplicacao:{multiplicacao}, raiz:{raiz}")