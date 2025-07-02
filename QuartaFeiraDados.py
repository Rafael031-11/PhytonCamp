from random import randint

user = int(input("Quantas jogadas são necessárias para os dados darem números iguais?: "))
jogadas = 0
dado1 = 1
dado2 = 2
while dado1 != dado2:
    jogadas += 1
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

if jogadas == user:
    print("Acertou!")
else:
    print(f'Foram necessárias {jogadas}, tente novamente.')