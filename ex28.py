import random
pc = random.randint(1, 5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
user = int(input("Em que número pensei: "))
print("PROCESSANDO...")
if user != pc:
    print(f"GANHEI! Eu pensei no número {pc} e não no {user}!")
else:
    print("PARABÉNS! Você conseguiu vencer")