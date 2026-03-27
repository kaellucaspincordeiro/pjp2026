def verificar_caldeira(temp_atual):

    if temp_atual < 90:
        return f"Aquecendo..."
    elif 90 <= temp_atual <= 100:
        return f"Pronta para uso"
    else:
        return f"PERIGO: Superaquecimento!"
    
temp_atual = float(input("Informe a sua temperatura para a caldeira: "))

temperatura_maquina = verificar_caldeira(temp_atual)
print(temperatura_maquina)