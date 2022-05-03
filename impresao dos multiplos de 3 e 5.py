x = int(input("Quantos numeros voce quer digitar?: "))
m = -1

for i in range(x):
  y = int(input("Digite um numero: "))
  if y > m:
    m = y
print("Este o maior numero que voce digitou:",m)