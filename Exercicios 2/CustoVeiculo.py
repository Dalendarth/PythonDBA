custo_fabrica = float(input('Digite o custo de fabrica do veiculo'))

if custo_fabrica <= 12000:
    distribuidor = custo_fabrica * 5 / 100
    print(f'O custo final para o consumidor é de: {distribuidor:.2f}')
elif custo_fabrica in range(12000, 25000):
    distribuidor = custo_fabrica * 10 / 100
    impostos = custo_fabrica * 10 / 100
    total = distribuidor + impostos
    print(f'O custo final para o consumidor é de {total:.2f} com {impostos:.0f}% e {distribuidor:.0f}% do distribuidor')
elif custo_fabrica >= 25000:
    distribuidor = custo_fabrica * 15 / 100
    impostos = custo_fabrica * 15 / 100
    total = distribuidor + impostos
    print(f'O custo final para o consumidor é de {total:.2f} com {impostos:.0f}% e {distribuidor:.0f}% do distribuidor')
else:
    print("Entrada invalida.")


