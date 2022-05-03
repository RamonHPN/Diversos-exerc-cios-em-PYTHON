while True:
    
  try:
      x = int(input("Digite o primeiro número "))
      break
  except ValueError:
      print("Por favor digite um número...")  
      continue

c = x // 100

if c % 4 == 0:
    print(f"O {c} é multiplo de 4")
else: print(f"O {c} não é multiplo de 4")