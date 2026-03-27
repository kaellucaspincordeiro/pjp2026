
def saudar_cliente():
    print("Bem-vindo à TechCoffee!")
    print("O que deseja pedir hoje?")

saudar_cliente()


def saudar_personalizado(nome):
    print(f"Olá, {nome}! Seu café favorito já está sendo preparado.")

saudar_personalizado("Seu Arnaldo")
saudar_personalizado("Seu Kael")

def soma(n1,n2):
    res = n1 + n2
    print(f"A soma entre {n1} e {n2} resulta em {res}")
soma(10,12)

def subtracao(n1,n2):
    res = n1 - n2
    print(f"A subtração entre {n1} e {n2} resulta em {res}")
subtracao(12,10)

def multiplicacao(n1,n2):
    res = n1 * n2
    print(f"A multiplicação entre {n1} e {n2} resulta em {res}")
multiplicacao(10,12)

def divisao(n1,n2):
    res = n1 / n2
    print(f"A divisão entre {n1} e {n2} resulta em {res:.2f}")
divisao(10,12)


def calcular_total(quantidade, preco_unitario):
    total = quantidade * preco_unitario
    return total

valor_da_venda = calcular_total(3, 5.50)
print(f"O valor a pagar é: R$ {valor_da_venda}")