"""
and (e), or(ou), not(não), is(é)

Operadores unários: not, is.
Operadores Binários: and, or.

Para o "and" ambos os valores precisam ser True
---------------------------------------------------------------
Para o "or" um ou outro valor precisa ser True
---------------------------------------------------------------
Para o "Not" o valor do booleano (condição) é invertido, ou seja, se for falso vira verdadeiro, se for verdadeiro
vira falso.
--------------------------------------------------------------
Para o "is" o valor é comparado com o segundo
"""

ativo = True
logado = True

if ativo and logado:
    print("Bem vindo usuario")
else:
    print("Você precisa ativar sua conta, por favor cheque seu e-mail")

    if ativo or logado:
        print("Bem vindo usuario")
    else:
        print("Você precisa ativar sua conta, por favor cheque seu e-mail")
"""
----------------------------------------------------------------------------
"""
#se nao estiver ativo
if not ativo:
    print("Você precisa ativar sua conta, por favor cheque seu e-mail ")
else:
    print("Bem vindo usuário")

print(not True)
print(not False)
"""
Exemplo is:
"""
if ativo is True:
    print("Você precisa ativar sua conta, por favor cheque seu e-mail ")
else:
    print("Bem vindo usuário")
"""
 ----------------------------------------------------------------------------
"""
#ativo é Falso?
print(ativo is False)


