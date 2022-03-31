lista = []
while True:
    n = int(input(('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso.")
        l = input("Quer continuar? [S/N]").upper()
        if l == 'S':
            continue
        else:
            break
    else:
        print("Valor duplicado! Não vou adicionar...")
        l = input("Quer continuar? [S/N]").upper()
        if l == 'S':
            continue
        else:
            print('-=-' * 20)
            print('Você digitou os valores', sorted(lista))
            break
