ordAtual = int(input("Insira o seu salário atual: "))
if ordAtual < 500:
    final = ordAtual + (ordAtual * 0.15)
    print(final)
elif ordAtual <= 1000:
    final = ordAtual + (ordAtual * 0.10)
    print(final)
else:
    final = ordAtual + (ordAtual * 0.05)
    print(final)


