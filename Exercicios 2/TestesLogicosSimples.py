x = 10
y = 5

print(x > y)  # Saída: True
print(x == y)  # Saída: False


a = True
b = False

print(a and b)  # Saída: False
print(a or b)  # Saída: True
print(not b)  # Saída: True

if True:
    print('Essa mensagem será exibida')

if False:
    print('Essa mensagem não será exibida')
""
""

# operador módulo % para verificar se o número é divisível por 2, se for é par, se não é impar:
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
""
""
num = int(input("Digite um número: "))

if num > 10:
    print("O número é maior do que 10.")
else:
    print("O número é menor ou igual a 10.")