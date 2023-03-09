"""
ESTRUTURAS CONDICIONAIS, IF (se), ELSE, ELIF
"""

idade = int(input("Digite uma idade:"))

"""
Estrutura condicional if em C

if (idade < 18){
    printf("menor de idade");
}
"""

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem Maioridade")
else:
    print("Maior de idade")

