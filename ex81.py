lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    q = input("Quer continuar ? [S/N]").upper()
    if q != 'S':
        break
print(f"Foram digitados {len(lista)} números!")
print(f"Lista ordenada de forma decrescente {sorted(lista, reverse=True)}")       
if 5 in lista:
    print("O valor 5 está na lista")
else:
    print('O valor 5 não está na lista')
        
