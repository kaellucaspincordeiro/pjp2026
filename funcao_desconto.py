def validar_cupom(codigo):

    if codigo == "CAFÉ10":
        return 0.10
    
    elif codigo == "PROMO5":
        return 0.05
    
    else:
        return 0


codigo = input("Informe o seu código de cupom: ").upper()
valor = float(input("Informe o seu valor para pagar: "))

cupom = validar_cupom(codigo)
total = valor - (valor * cupom)
print(f"O total para pagar é de R${total:.2f}")