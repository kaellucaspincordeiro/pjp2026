def calcular_item(preco_unitario, quantidade):

    total = quantidade * preco_unitario
    imposto = total * 0.05
    return total + imposto 

preco_unitario = float(input("Informe o seu preço para pagar o imposto: "))
quantidade = int(input("Informe a sua quantidade: "))

imposto = calcular_item(preco_unitario, quantidade)
print(f"O cliente para pagar com {quantidade} itens ficaria R${imposto:.2f}")