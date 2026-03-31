nome_convidados = ["Adriano", "Carlos", "Darlene", "Daici", "Gustavo", "Kael", "Moacir", "Leonardo", "Luis", "Rodrigo", "Ricardo"]

nome = input("Digite um nome: ")

if nome in nome_convidados:
    print(f"Bem-vindo! Nome na lista.")
else:    
    print(f"Desculpe, seu nome não consta aqui.")