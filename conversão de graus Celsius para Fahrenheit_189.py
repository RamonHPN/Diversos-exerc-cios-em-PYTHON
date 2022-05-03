x = int(input("entre com um número: "))
if x>= 15:
  for i in range(1,x):
    if i%3==0 and i%5==0:
      print(i)
else:
  print("Digite um número maior ou igual a 15")