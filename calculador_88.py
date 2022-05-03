x = input("Digite o primeiro número: ")
y = input("Digite o segundo número: ")
op = input("Digite a operacao desejada (soma, sub, mult, div): ")


if open == "soma":
	r = int(x) + int(y)
elif op == "sub":
	r = int(x) - int(y)
elif op == "mult":
	r = int(x) * int(y)
elif op == "div":
	r = int(x) / int(y)
else:
	r = "Operação inválida"
    
print("O resultado da operação é: " + str(r))