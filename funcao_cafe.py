def descrever_pedido(tamanho, tipo_grao):
    return f"Preparando um café {tamanho} com grãos do tipo {tipo_grao}."


tamanho = input("Informe o tamanho do seu copo para o café: 'Pequeno', 'Médio', 'Grande' \n")
tipo_grao = input("Informe o tipo do grão de café: \n")

chegada_pedido = descrever_pedido(tamanho, tipo_grao)
print(chegada_pedido)

    
