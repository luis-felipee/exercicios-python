import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
player = int(input('''[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA: 
'''))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
if player == computador:
    print('-=-' * 20)
    print("Empate!")
    print('-=-' * 20)
elif (player == 0 and computador == 2) or (player == 2 and computador == 1) or (player == 1 and computador == 0):
    print('-=-' * 20)
    print(f"Você ganhou! computador escolheu {itens[computador]} e você {itens[player]}")
    print('-=-' * 20)