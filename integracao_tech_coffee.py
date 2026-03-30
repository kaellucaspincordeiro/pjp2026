from funcao_calculo_imposto import calcular_item
from funcao_fidelidade import gerar_pontos

preco_unitario = float(input("Informe o preço do café: "))
quantidade = int(input("Informe a sua quantidade: "))

imposto = calcular_item(preco_unitario, quantidade)
pontos = gerar_pontos(imposto)

print(f"Valor final: R${imposto:.2f} | Pontos ganhos: {pontos}")
