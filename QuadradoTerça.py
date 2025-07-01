
lado = int(input("Insira o valor de um lado do seu quadrado: "))
if lado == str:
    print("Apenas números ! ")
    quit()
Perimetro = lado * 4
print(f'O perímetro do seu quadrado é: {Perimetro}')
Area = lado ** 2
print(f'A área do seu quadrado é: {Area}')