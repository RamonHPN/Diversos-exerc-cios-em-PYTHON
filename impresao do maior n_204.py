x = int(input("Digite o primeiro numero "))
y = int(input("Digite o segundo numero "))
z = int(0)

for i in range (3, 10):
    if(i % 2 == 0):
        z = y - x
    else:
        z = y + x
    
    x = y
    y = z
    
    print(z)