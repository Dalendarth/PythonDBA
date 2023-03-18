
s = input("Digite o sexo masculino ou feminino F/M:").lower()#usei lower p/ o usuario digitar minuscula ou maiuscula!
alt = float(input("Digite a altura em metros"))

if s == "m":
    PesoIdeal = (72.7 * alt) - 58
    print(f"O peso ideal para um homem com {alt}m de altura é de {PesoIdeal}kg. ")
elif s == "f":
    PesoIdeal = (62.1 * alt) - 44.7
    print(f"O peso ideal para uma mulher com {alt}m de altura é de {PesoIdeal}kg")
else:
    print("Sexo invalido, pressione M para masculino ou F para feminino.")






