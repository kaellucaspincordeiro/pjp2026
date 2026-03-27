soma = 0

for i in range(1,5):
    
    nota = float(input("Nota do aluno: "))
    
    soma += nota

media = soma/4
print(f"A média ficou: {media}")
