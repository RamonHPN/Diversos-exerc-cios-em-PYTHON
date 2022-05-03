while True:
  try:
      x = int(input("Digite o primeiro numero "))
      y = int(input("Digite o segundo numero "))
      break
  except ValueError:
      print("Por favor digite um número...")  
      continue
  
while True:
    try:
        print("dividendo: ", x)
        print("divisor: ", y)
        print("quociente: ", x//y)
        print("resto:", x%y)
    except ZeroDivisionError:
        print("Divisão por zero? Não fazemos isso aqui!")
        x = int(input("Digite o primeiro numero "))
        y = int(input("Digite o segundo numero "))
        continue
    break