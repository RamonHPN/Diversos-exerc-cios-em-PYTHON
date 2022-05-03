import math
while True:
    try:
        x = float(input("Digite o primeiro numero "))
        print("logaritmo: ", math.log(x,10))
        break
    except ValueError:
        print("Por favor digite um número...Um numero positivo!!!")
        continue