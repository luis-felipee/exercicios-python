lista = list()
listaImpar = list()
listaPar = list()
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        listaPar.append(n)
    if n % 2 != 0:
        listaImpar.append(n)
    q = input("Quer continuar? [S/N] ").upper()
    if q != 'S':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')