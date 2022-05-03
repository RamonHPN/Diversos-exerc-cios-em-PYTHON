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
    
elif (x > y and x > z):
    maior = x**2  
    lados = y**2 + z**2

elif(y > z):
    maior = y ** 2 
    lados = x ** 2 + z ** 2
else:
    maior = z ** 2 
    lados = x ** 2 + y ** 2

if maior == lados:
    print("É um triângulo retangulo")
elif maior > lados:
    print("É um triângulo obtusangulo")
else:
    print("É um triângulo acutangulo")