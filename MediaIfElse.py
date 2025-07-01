nota1 = int(input("Insira a sua primeira nota: "))
nota2 = int(input("Insira a sua segunda nota: "))
media = (nota1 + nota2) / 2
if media <= 30:
    print("Insuficiente.")
    quit()
    if media <= 60:
        print("Suficiente.")
        quit()
        if media >= 70:
            print("Bom")
            quit()