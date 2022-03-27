count = 0
soma = 0
l = []
while True:
    n = int(input("Digite um número: "))
    count += 1
    soma += n
    l.append(n)
    q = input("Quer continuar: ").upper()
    if q == 'S':
        continue
    else:
        break
print(f"Você digitou {count} números e a média foi {soma / n}")
print(f"O maior valor foi {max(l)} e o menor foi {min(l)}")