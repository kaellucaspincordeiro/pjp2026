numeros = []

for num in range(5):

    num = int(input("Informe seu número: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)

print(f"Maior número - {maior}, menor número - {menor}, soma - {soma}, média - {media}")