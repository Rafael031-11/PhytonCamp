from datetime import date

NascimentoPergunta = int(input("Insira a sua data de nascimento: "))
idadeExercito = date.today().year - NascimentoPergunta
if idadeExercito < 18:
    print("Ainda não tens idade para o recenseamento.")
elif idadeExercito <= 55:
    print("Está no momento para o recenseamento.")
else:
    print("Já passou o prazo para o recenseamento.")