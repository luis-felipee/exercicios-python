count = 0
s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    count += 1
    s += n
print(f"{count} números foram digitados. A soma entre eles é {s}")