while True:
  try:
    n = float(input('Digite um número: '))
    break
  except ValueError:
      print("Por favor digite um número")  
      continue

x = n * (1/3)

print('A terça parte de {:.2f} é {:.2f}'.format(n, x))