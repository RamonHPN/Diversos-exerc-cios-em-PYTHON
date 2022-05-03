while True:
  try:
      x = int(input("Digite a primeira nota "))
      y = int(input("Digite a segunda nota "))
      z = int(input("Digite a terceira nota "))
      break
  except ValueError:
      print("Por favor digite um número...")  
      continue
if x<y+z and y<x+z and z<x+y:
    print("Podem ser lados de um triângulo")
else:
    print("Não podem ser lados de um triângulo")