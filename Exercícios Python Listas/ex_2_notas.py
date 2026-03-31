notas = [4.5, 7.0, 8.5, 5.0, 10, 6.5, 9.0, 3.0, 7.5, 6.0]
aprovados = []
reprovados = []

for nota in notas:
    if nota >= 7:
        aprovados.append(nota)
    elif nota < 7:
        reprovados.append(nota)

print(f"As notas dos alunos aprovados foram {aprovados}\n")
print(f"As notas dos alunos reprovados foram {reprovados}")