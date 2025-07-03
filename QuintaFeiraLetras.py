frase = (input("Entre com a frase: "))
letra = (input("Qual letra deseja verificar?: "))

contador = 0
for x in frase:
    if x == letra:
        contador += 1

if contador == 0:
    print("Não foi encontrada a letra.")
else:
    print(f'A letra {letra} foi encontrada {contador} vezes.')