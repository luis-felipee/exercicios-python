mais18 = h = m = 0
while True:
    idade = int(input("Idade da pessoa: "))
    sexo = str(input("Sexo da pessoa [F/M] ")).upper()
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    continuar = input("Quer continuar? [S/N]").upper()
    if continuar == 'S':
        continue
    elif continuar != 'S':
        break
print(f"{mais18} pessoas com mais de 18 anos.")
print(f"{h} homens cadastrados.")
print(f"{m} mulheres com menos de 20 anos")