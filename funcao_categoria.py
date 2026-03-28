def definir_categoria(codigo_produto):

    codigo_produto = codigo_produto.upper()

    if codigo_produto.startswith("BEB"):
        return "Bebida Quente"
    elif codigo_produto.startswith("COM"):
        return "Comida/Salgado"
    else:
        return "Código indefinido para categoria"
    
categoria = definir_categoria("comida")
print(categoria)