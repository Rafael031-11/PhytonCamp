Velocidade = int(input("A que  velocidade o seu veículo passou pê-lo radar?: "))
Multa = Velocidade - 80

if Velocidade > 80:
    print(f'Está acima do limite permitido. A multa foi gerada no valor de {Multa * 2} euros.')
else:
    print("Dentro do limite. Boa viagem.")
