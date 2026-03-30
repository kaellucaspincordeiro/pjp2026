def calcular_item(preco_unitario, quantidade):

    total = quantidade * preco_unitario
    imposto = total * 0.05
    return total + imposto