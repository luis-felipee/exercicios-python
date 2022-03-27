import random
count = 0
vitoria = 0
while True:
    print("-=-" * 20)
    print("VAMO JOGAR PAR OU ÍMPAR")
    print("-=-" * 20)
    
    n = int(input("Diga um valor: "))
    p = str(input("Par Ou Ímpar? [P/I]")).upper()
    pc = random.randint(1, 10)
    soma = n + pc
    count += 1
    if soma % 2 == 0 and p == 'P':
        print(f"VOCÊ GANHOU! você jogou {n} e o computador {pc}. Total de {soma} DEU PAR!")
        vitoria += 1
    elif soma % 2 != 0 and p == 'I':
        print(f"VOCÊ GANHOU! você jogou {n} e o computador {pc}. Total de {soma} DEU IMPAR!")
        vitoria += 1
    else:
        print(f"VOCÊ PERDEU! você jogou {n} e o computador {pc}. Total de {soma}")
        break
    continue
print(f"Você ganhou {vitoria} vezes consecutivas.")