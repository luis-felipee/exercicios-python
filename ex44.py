valor = float(input("Valor do produto: "))
pagamento = input("[1] para pagamento à vista,[2] à vista no cartão, [3] para em até 2x no cartão, [4] para 3x ou mais no cartão.")
if pagamento == '1':
    print(f"Á vista com 10% de desconto, o valor ficou R${valor - (valor * 10 / 100) :.2f}")
elif pagamento == '2':
    print(f"Á vista NO CARTÃO 5% de desconto, o valor ficou R${valor - (valor * 5 / 100) :.2f}")
elif pagamento == '3':
    print(f"Em até 2x no cartão, preço normal:  R${valor :.2f}")
elif pagamento == '4':
    print(f"Em 3x ou mais no cartão, 20% de juros:  R${valor + (valor * 20 / 100) :.2f}")