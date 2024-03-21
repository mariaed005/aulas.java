print("Programa para calcular média dos alunos")
executar = True

while executar:
    print ("Digite seu nome")
    nome = input()

    print(" Digite sua primeira nota")
    nota_1 = float(input()) 

    print("Digite sua segunda nota ")
    nota_2 = float(input())

    print("Digite sua terceira nota")
    nota_3 = float(input())

    print("Digite sua quarta nota")
    nota_4 = float(input())

    media = (nota_1 + nota_2 + 
            nota_3 + nota_4) / 4 

    print("Nome         Nota 1          Nota 2          Nota 3         Nota 4          Média Final")
    print (f"{nome :<12}{nota_1:<16}{nota_2:<16}{nota_3:<16}{nota_4:<16}{media:<21}")

    print("Deseja executar novamente (S/N)")
    novamente = input()
    if novamente == 'n':
        break

print("Fim do programa")



    





