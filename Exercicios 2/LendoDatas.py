data_mes = int(input("Digite um mes: "))
data_dia = int(input("DIgite um dia do mes: "))
# coloquei o dicionario abaixo para rodar o codigo e ler a data de maneira eficiente
meses = {
    "janeiro": 1,
    "fevereiro": 2,
    "março": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12,
}

if data_mes in meses.values():
    nome_mes = list(meses.keys())[list(meses.values()).index(data_mes)]
    print(f"Mês selecionado: {nome_mes}")
elif data_dia % 4:
    print("Data válida!")
else:
    print("Data inválida!")
