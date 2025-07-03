inicial = int(input("Insira o primeiro número: "))
final = int(input("Insira o segundo número: "))

if inicial % 2 != 0:
    inicial += 1

for x in range(inicial, final, 2):
    print(x)