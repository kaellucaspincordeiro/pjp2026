res = 1

num = int(input("Informe o seu número para o fatorial: "))

for fat in range(1, num + 1):
    
    res = res * fat

print(f"O fatorial de {num}! é {res}")
