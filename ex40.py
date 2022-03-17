n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
if media < 5.0:
    print(f"COM A MÉDIA DE {media}, VOCÊ FOI REPROVADO!")
elif media >= 5.0 and media <= 6.9:
    print(f"COM A MÉDIA DE {media}, VOCÊ ESTÁ DE RECUPERAÇÃO!")
elif media >= 7.0:
    print(f"COM A MÉDIA DE {media}, VOCÊ FOI APROVADO!")
