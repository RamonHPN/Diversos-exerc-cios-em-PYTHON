data = 00000000
mes = 0
ano = 0
dia = 0

data = int(input("digite a data no formato ddmmaaaa"))
    
dia = data // 1000000
mes = (data % 1000000) // 10000
ano = data %10000

print("dia = ", dia)
print("mes = ", mes)
print("ano = ", ano)