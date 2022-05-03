n = 0
cent = 0
dez = 0
while True:
    try:
        n = int(input('Entre com um número de três casas '))
        break
    except ValueError:
        print("Por favor digite um número")
        continue
    
while True:
    if n <= 999 and n >= 100:
        cent = n/100
        rest = n % 100
        dez = rest // 10
        print('Algarismo da casa das dezenas: ', dez)
        break
    else:
        print("Entre com um número de três casas por favor")
        n = int(input('Entre com um número de três casas '))
        continue