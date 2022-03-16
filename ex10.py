money = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = money / 5.16
print('Com R${:.2f} você pode comprar US${:.2f} '.format(money, dolar))