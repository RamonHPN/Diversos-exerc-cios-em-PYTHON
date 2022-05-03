while True:
    try:
        x = float(input('Primeiro número: '))
        y = float(input('Segundo  número: '))
        z = float(input('Terceiro número: '))
        break
    except ValueError:
        print("Por favor digite um número...")  
        continue
    
if (x + y < z) or (x + z < y) or (y + z < x):
    print('Nao é um triangulo')
elif (x == y) and (x == z):
    print('Equilatero')
elif (x == y) or (x == z) or (y == z):
    print('Isósceles')
else:
    print('Escaleno')