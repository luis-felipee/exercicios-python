import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("terceiro aluno: "))
n4 = str(input("quarto aluno: "))
lista = [n1, n2, n3, n4]
rand = random.choice(lista)
print(f"O aluno escolhido foi: {rand}")