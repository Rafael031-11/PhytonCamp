from time import sleep

Num = int(input("Insira um número: "))

for x in range(1, 11):
    print('{} x {} = {}'.format(Num,x, x*Num ))
    sleep(0.3)