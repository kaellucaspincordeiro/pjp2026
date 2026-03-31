notas = [4.5, 7.0, 8.5, 5.0, 10, 6.5, 9.0, 3.0, 7.5, 6.0]
aprovado = []
reprovado = []

for nota in notas:
    if nota >= 7:
        aprovado.append(nota)
    elif nota < 7:
        reprovado.append(nota)

print(f"As notas dos alunos aprovados foram {aprovado}\n")
print(f"As notas dos alunos reprovados foram {reprovado}")