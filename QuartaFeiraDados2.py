from random import randint

from QuartaFeiraDados import jogadas

Resposta = int(input("Quantas jogadas são necessárias para os dados darem números iguais?: "))
jogadas = 0
dado1 = 1
dado2 = 2
while True:
    jogadas += 1
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    if dado1 == dado2:
        break

if Resposta == jogadas:
    print("Acertou!")
else:
    print("Tente novamente!")