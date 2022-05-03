while True:
  try:
      x = float(input("Digite a primeira nota "))
      y = float(input("Digite a segunda nota "))
      break
  except ValueError:
      print("Por favor digite um número...")  
      continue

print("A media dos números é:", (x+y)/2)