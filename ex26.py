nome = str(input("Digite seu nome : ")).lower()
print("A aparece {}".format(nome.count('a')))
print(" A primeira letra A aparece na posição {} ".format(nome.find('a')))
print("A última letra A apareceu na posição {} ".format(nome.rfind('a')))