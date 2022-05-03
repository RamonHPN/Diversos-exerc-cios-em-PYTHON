import math
while True:
  try:
      x = float(input("Digite o primeiro numero "))
      a = math.sin(math.radians(x))
      b = math.cos(math.radians(x))
      c = math.tan(math.radians(x))
      d = 1/(math.sin(math.radians(x)))
      e = 1/(math.cos(math.radians(x)))
      f = 1/(math.tan(math.radians(x)))
      break
  except ValueError:
      print("Por favor digite um número...")  
      continue

print("o angulo de {} tem o seno de {:.2f} ".format(x, a))
print("o angulo de {} tem o cosseno de {:.2f} ".format(x, b))
print("o angulo de {} tem o tangente de {:.2f} ".format(x, c))
print("o angulo de {} tem a secante de {:.2f} ".format(x, e))
print("o angulo de {} tem a cosecante de {:.2f} ".format(x, d))
print("o angulo de {} tem o cotangente de {:.2f} ".format(x, f))