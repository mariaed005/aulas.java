print("Programa para calcular área de um retangulo")
while True:

    print("Informe o tamanho da base em centímetros")
    base = float (input())

    # input() ==> "42"
    # float ( "42" ) ==> "42.0"

    print("Informe a altura do retangulo em centimetros")
    altura = float(input())
    area = base*altura
    print(f"O tamanho da area é: {area:6.2f} cm²")

    print("Deseja executar novamente (S/N):")
    novamente = input()
    if novamente == 'N':
        break

print("Fim do programa")

