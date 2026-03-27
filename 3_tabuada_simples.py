cont = 0

n = int(input("Informe o seu número para a tabuada: "))

while cont < 10:
    
    cont += 1
    res = n * cont
    print(f"{n} X {cont} = {res}\n")
