while True:
    
  try:
      x = int(input("Digite o primeiro número "))
      break
  except ValueError:
      print("Por favor digite um número...")  
      continue

if x % 10 == 0:
    print("É multiplo de 10.\n")
if x % 5 == 0:
    print("É multiplo de 5.\n")
if x % 2 == 0:
    print("É multiplo de 2.\n")
if x % 10 != 0 and x % 5 != 0 and x % 2 !=0:
    print("Nao é multiplo de 10, 5 ou 2.\n")