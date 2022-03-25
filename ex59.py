while True:
    n1 = int(input("Digite o 1º número: "))
    n2 = int(input("Digite 2º número: "))
    p = int(input("[1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa: "))
    if p == 1:
        print(f"A soma entre {n1} e {n2} é: {n1 + n2}")
    elif p == 2:
        print(f"A multiplicação entre {n1} e {n2} é: {n1 * n2}")
    elif p == 3:
        if n1 > n2:  
            print(f"O maior entre eles é o {n1}")
        elif n2 > n1:
            print(f"O menor entre eles é o {n2}")
        else:
            print("Os dois são iguais!")
        break
    elif p == 4:
        print("Adicione novos números.")
        print("-=-" * 20)
        continue
    elif p == 5:
        print('-=-' * 20)
        print("SAINDO DO PROGRAMA...")
        break
print("All done")