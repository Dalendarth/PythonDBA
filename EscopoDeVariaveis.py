"""
Escopo de Variaveis

Dois casos de escopo:

1- Variaveis Globais:
   -Variaveis Globais são reconhecidas, ou seja seu escopo compreende todo o programa.

2- Variaveis Locais:
   -Variaveis Locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
   está limitado ao bloco onde foi declarada.

Para declarar variaveis em python faz da seguinte maneira:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declarar uma variavel, não coloca-se o
tipo de dado dela, este tipo, é inferido ao atribuir o valor ao mesmo.
"""

numero = 42 # exemplo de variavel global
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10
    print(novo)
