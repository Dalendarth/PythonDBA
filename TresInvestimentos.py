# Lê o valor investido por cada amigo
investimento1 = float(input("Digite o valor investido pelo primeiro amigo: "))
investimento2 = float(input("Digite o valor investido pelo segundo amigo: "))
investimento3 = float(input("Digite o valor investido pelo terceiro amigo: "))

# Soma o valor total investido
total_investido = investimento1 + investimento2 + investimento3

# Lê o valor do prêmio
premio = float(input("Digite o valor do prêmio: "))

# Calcula a porcentagem do prêmio para cada amigo
porcentagem1 = investimento1 / total_investido
porcentagem2 = investimento2 / total_investido
porcentagem3 = investimento3 / total_investido

# Calcula o valor do prêmio para cada amigo
ganho1 = premio * porcentagem1
ganho2 = premio * porcentagem2
ganho3 = premio * porcentagem3

# Imprime o resultado
print(f"O primeiro amigo ganharia R$ {ganho1:.2f}")
print(f"O segundo amigo ganharia R$ {ganho2:.2f}")
print(f"O terceiro amigo ganharia R$ {ganho3:.2f}")