"""
faça um programa para ler as dimensões de um terreno(comprimento C e largura L), bem como o preço do metro de tela.
imprima o custo para cercar esse mesmo terreno com tela
"""

c = float(input("Digite o comprimento: "))
l = float(input("Digite a largura: "))
p = float(input("Digite o preço da tela: "))

area = c * l ### calcula a area do terreno
preco = area * p

print(f"o custo total para cercar o terreno é de: {preco:.2f}")