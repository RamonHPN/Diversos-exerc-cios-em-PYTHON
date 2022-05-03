while True:
  try:
      x = float(input("Digite o primeiro numero "))
      y = float(input("Digite o segundo numero "))
      w = float(input("Digite o terceiro numero "))
      z = float(input("Digite o quarto numero "))
      break
  except ValueError:
      print("Por favor digite um número...")  
      continue
  
print("A media dos ponderada números é:", (x*1 + y*2 + w*3 + z*4)/10)