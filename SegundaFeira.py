def mais(n1, n2):
    return n1 + n2

def menos(n1, n2):
    return n1 - n2

def vezes(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

n1 = int(input("Qual é o primeiro número? "))
n2 = int(input("Qual é o segundo número? "))
op = input("Qual é a operação? (+ ou -) ")

if op == "+":
    mais(n1, n2)
elif op == "-":
    menos(n1, n2)
elif op == "x":
    vezes(n1, n2)
else:
    divisao(n1, n2)
    print()