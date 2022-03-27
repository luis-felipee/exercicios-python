count = 0
soma = 0
while True:
    try:
        n = int(input("Digite um número [999] para parar: "))
        count += 1
        soma += n
        if n != 999:
            continue
        else:
            count -= 1
            soma -= 999
            break
    except:
        print("Digite um número!")
        continue
print(f"Você digitou {count} números e a soma entre eles foi {soma}.")
print("FIM")