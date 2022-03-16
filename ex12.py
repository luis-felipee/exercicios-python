preco = float(input("Qual é o preço do produto? R$"))
porcentagem = 5.0 / 100
valorFinal = preco - (porcentagem * preco)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, valorFinal))