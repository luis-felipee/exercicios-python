from ast import Num


soma = 0
count = 0
for i in range(1, 7):
    n = int(input("Digite o {} valor:  ".format(i)))
    soma = soma + n
    count = count + 1
print("Você informou {} números e a soma foi {}".format(count, soma))