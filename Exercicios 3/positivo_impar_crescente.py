num = int(input('Digite um numero impar:'))

if num % 2 == 0:
    num += 1
    for i in range(num, num + 10, 2):
        print(i)