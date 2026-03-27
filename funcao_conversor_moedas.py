def converter_para_dolar(valor_reais):
    return valor_reais/5

valor_reais = float(input("Informe o seu valor real para conversão do valor dólar: "))
conversao_dolar = converter_para_dolar(valor_reais)
print(f"A conversão de real para dólar ficaria US$ {conversao_dolar:.2f}")