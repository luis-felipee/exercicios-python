import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("terceiro aluno: "))
n4 = str(input("quarto aluno: "))
list = [n1, n2, n3, n4]
random.shuffle(list)
print(f"A ordem é {list}")