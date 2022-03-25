list = []
for i in range(1, 6):
    peso = float(input(f"Peso da {i}ª pessoa: "))
    list.append(peso)
print(f"O maior peso lido foi de {max(list)}Kg")
print(f"O menor peso lido foi de {min(list)}Kg")
    