


salario_base = float(input("Digite o salário base: "))

gratificacao = salario_base * 0.5

salario_com_gratificacao = salario_base + gratificacao

imposto = salario_com_gratificacao * 0.7

salario_final = salario_com_gratificacao - imposto

print(f"O salário final, incluindo gratificação e impostos, é de: {salario_final:.2f}")