x = int(input("entre com a temperatura maior em Fahrenheit: "))
y = int(input("entre com a temperatura menor em Fahrenheit: "))
y=y-1
dec = int(input("entre com decremento: "))
dec = dec*-1

for i in range(x,y,dec):
  print("Temperatura em Fahrenheit", i)
  C = 5 * (i - 32)/9
  print("Temperatura em Celsius", C)