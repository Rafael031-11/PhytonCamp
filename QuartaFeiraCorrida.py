from datetime import date

NascimentoPergunta = int(input("Insira a sua data de nascimento: "))
idadeCategorias = date.today().year - NascimentoPergunta

if idadeCategorias < 9:
    print("Está na classe Benjamin.")
elif idadeCategorias <= 14:
    print("Está na classe Infantil.")
elif idadeCategorias <= 19:
    print("Está na classe Júnior.")
elif idadeCategorias <= 25:
    print("Está na classe Sénior")
else:
    print("Está na classe Master")
