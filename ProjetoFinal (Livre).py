import random

Perguntas = {
    "Pergunta1": "Quem foi o primeiro rei de Portugal?",
    "1" : "D. Afonso Henriques.",
    "2" : "D. João I.",
    "3" : "D. Dinis.",
    "4" : "D. Manuel I.",

    "Pergunta2": "Qual destes rios é o mais longo em Portugal?",
    "5" : "Rio Douro.",
    "6" : "Rio Tejo.",
    "7" : "Rio Guadiana.",
    "8" : "Rio Mondego.",

    "Pergunta3": "Qual destes escritores portugueses é conhecido por “Os Lusíadas”?",
    "9" : "Fernando Pessoa",
    "10" : "José Saramago",
    "11" : "Luís de Camões",
    "12" : "Eça de Queirós."

}




print(Perguntas["Pergunta1"])

for x in range(1, 5):
    print(f"{x} - {Perguntas[str(x)]}")

print()

print(Perguntas["Pergunta2"])
for x in range(5, 9):
    print(f"{x} - {Perguntas[str(x)]}")

print()

print(Perguntas["Pergunta3"])
for x in range(9, 13):
    print(f"{x} - {Perguntas[str(x)]}")
