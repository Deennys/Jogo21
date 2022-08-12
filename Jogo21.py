import random


def cria_baralho():
    bar = []
    for naipe in ('♦', '♤', '♧', '♥'):
        for valor in range(1,14):
            c = (valor, naipe)
            bar.append(c)
    return bar

def comprar(deck):
    return deck.pop()

def distribui(qtd, deck):
    mao = []
    while qtd > 0:
        mao.append(comprar(deck))
        qtd -= 1
    return mao

def embaralhar(deck):
    qtd = random.randint(200, 1000)

    while qtd > 0:
        i = random.randint(0,51)
        j = random.randint(0, 51)

        aux = deck[i]
        deck[i] = deck[j]
        deck[j] = aux
        qtd -= 1

def soma_pontos(mao):
    soma = 0
    for c in mao:
        if c[0] > 10:
            soma = soma + 10
        else:
            soma = soma + c[0]
    return soma

baralho = cria_baralho()
embaralhar(baralho)

humano = distribui(2, baralho)
cpu = distribui(2, baralho)
print(humano)
resp = input("Quer mais cartas (s/n)?")
while resp == 's':
    c = comprar(baralho)
    humano.append(c)
    print(humano)
    resp = input("Quer mais cartas (s/n)?")

while soma_pontos(cpu) < 17:
    cpu.append(comprar(baralho))

print(cpu)