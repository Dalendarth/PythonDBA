caractere = 10
vetor = []

for i in range(caractere):
    letra = input('Digite um caractere: ')
    if letra.lower() in 'aeiou':
        print(f'O caractere digitado ({letra}) é uma vogal.')
        vetor.append(letra)
    else:
        print(f'O caractere digitado ({letra}) é uma consoante.')

print(f'Caracteres a seguir: {vetor}')
