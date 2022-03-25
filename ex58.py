import random
cont = 0
user = None
pc = random.randint(1, 11)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)

#
print("PROCESSANDO...")
while True:
    user = int(input("Em que número pensei: "))
    cont = cont + 1
    if user != pc:
        print("Errou! Tente novamente!")
    else:
        print(f"Você acertou em {cont} chances!")
        break
print("All done")
