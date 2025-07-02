import random

nums = random.randint(1, 5)
Respos = int(input("Escolha um número entre 1 e 5: "))
if Respos == nums:
    print("Parabéns! Você acertou.")
else:
    print("Você errou! Tente novamente.")
    print(f'O número era: {nums}')