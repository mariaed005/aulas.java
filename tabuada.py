print("Programa da tabuada")

print("Por favor, digite um numero")
numero = int(input())

i = 1   #inicialização

while i <= 10:   #condição
    res = numero* i
    print(f"{numero} x {i:>2} = {res:>2} ")
    i = i + 1   #incremento
    

