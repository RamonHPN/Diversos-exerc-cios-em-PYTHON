import math
while True:
    try:
        x = float(input("Digite o primeiro numero "))
        y = int(input("Digite a base do logaritmo "))
        break
    except ValueError:
        print("Por favor digite um número...Um numero positivo!!!")
        continue
while True:
    try:
        print("logaritmo: ", math.log(x,y))
        break
    except ZeroDivisionError:
        print("A base tem que ser diferente de 1")
        x = float(input("Digite o primeiro numero "))
        y = int(input("Digite a base do logaritmo "))
        continue
    break