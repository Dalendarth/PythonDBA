"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

Import this

Aideia da PEP8 é que possamoas escrever codigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minusculo separados por underline para funções ou variáveis;

def soma ():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize quatro espaços para identação! (importante)

if 'a' in 'banana':
    print ('tem')

[4] - Linhas em branco;

-Separar Funções e definições de classes com duas linhas em branco;
-Métodos dentro de uma classe devem ser separados dentro de uma classe com uma única linha em branco;

[5] - Imports

- Imports devem sempre ser feitos em linhas separadas;

#Import Errado

import sys, os

#Import Certo

Import sys
Import os

#Não há problemas em utilizar from types import StringType ListType

#Caso tenha muitos Imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType,
)
# Imports devem ser colocados no topo do arquivo logo depois de quaisquer comentários ou docstrings e
#antes de constantes ou variáveis globais.

 [6] - Espaços em expressões e instruções

 #Não Faça:

funcao ( algo[ 1 ], { outro:  2 }  )

#Faça:

funcao (algo[1], {outro: 2})

#Não Faça:

algo (1)

#Faça:

algo(1)

#Não Faça:

dict ['chave'] = lista [indice]


#Faça:

dict['chave'] = lista[indice]

#Não Faça:

x              = 1
y              = 3
variavel_longa = 5

#Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha;

exemplo:

import this

print ('algo')

 """

