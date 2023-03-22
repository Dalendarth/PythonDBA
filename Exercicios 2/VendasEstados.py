

valor = float(input("Digite o valor de um produto:"))
print("Selecione um estado")

print("1 - MG")
print("2 - SP")
print("3 - RJ")
print("4 - MS")

estado = input().lower()
if estado == 'mg':
    print("Estado selecionado: Minas Gerais")
    porc = valor * (1 + 7 / 100)
    print(f"O valor do produto com o acrescimo estadual é de: {porc}")
elif estado == 'sp':
    print("Estado selecionado: São Paulo")
    porc = valor * (1 + 12 / 100)
    print(f"O valor do produto com acrescimo estadual é de: {porc}")
elif estado == 'rj':
    print("Estado Selecionado: Rio de Janeiro")
    porc = valor * (1 + 15 / 100)
    print(f"O valor do produto com acrescimo estadual é de: {porc}")
elif estado == 'ms':
    print("Estado selecionado: Mato Grosso do Sul")
    porc = valor * (1 + 8 / 100)
    print(f"O valor do produto com acrescimo estadual é : {porc}")
else:
    print("Entrada Invalida.")





