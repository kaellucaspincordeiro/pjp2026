nota = 11

while nota < 0 or nota > 10:
    
    nota = float(input("Informe a sua nota: "))
    
    if nota == 11:
        print(f"A sua nota informada está inválida! Digite novamente a nota para validar.\n")
    else:
        print(f"A sua nota informada está válida!")