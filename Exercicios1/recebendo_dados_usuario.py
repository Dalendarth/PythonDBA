"""
Recebendo dados do usuário

input() -> Todo o dado recebido via input é do tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas Duplas Triplas

Exemplos:

- Aspas simples -> 'nome'
- Aspas duplas -> "nome"
- Aspas simples triplas -> '''nome'''

comandos sob strings e variáveis:
print -> (imprimir)
f/format -> (escreva)
"""
#- Aspas duplas triplas -> """nome"""

#Entrada de dados
#print("Qual seu nome?")
#nome = input() #Input significa entrada do teclado

nome = input('Qual seu nome?')


#Exemplo de print antigo versão 2x do python
#print('Seja bem vindo(a) %s' % (nome))

#Exemplo de print 'moderno' versão 3.0 do python
#print('Seja bem vindo(a){0}'.format(nome))

#print('O(A) {0} tem {1} anos'.format(nome, idade))

#Exemplo de print 'mais atual' a partir da versão 3.7 do python
print(f'Seja bem vindo(a){nome}')

#print('Qual sua idade?')
#idade = input()
#Processamento

idade = input('Qual sua idade?')

#Saída
#Exemplo de print antigo versão 2x do python
#print('O(A) %s tem %s anos' % (nome, idade)) #A porcentagem representa/declara a variável dentro da linha de codigo
#nesse caso duas porcentagens uma representando nome e outra idade;

#Exemplo de print 'mais atual' a partir da versão 3.7 do python
print(f'O(A) {nome} tem {idade} anos')
"""
#  int(idade) => cast 
Cast é a conversão de um tipo de dado para outro;
Cast pode ser usado na linha 46 da seguinte forma -> idade = int (input('Qual sua idade?')), o resultado é abreviado
"""
print(f'O(A) {nome} nasceu em {2022 - int (idade)}')