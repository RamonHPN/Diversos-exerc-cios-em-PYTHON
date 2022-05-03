y = str(input("Entre com o seu nome: ")).strip()
n = y.split()
x = n[0]
if x == "JOSÉ" or x == "José" or x == "josé":
    print(x)
else:
    print("FIM")