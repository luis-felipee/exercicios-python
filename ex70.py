total = produto = menor =   0
cont =  0
barato = ''
while True:
    nome = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    total += preco
    cont += 1
    if preco > 1000:
        produto += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    continuar = input("Quer continuar? [S/N]").upper()
    if continuar == 'S':
        continue
    else:
        break
print(f'Você comprou {cont} produtos')
print(f'O total da compra foi R${total}')
print(f'Temos {produto} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')