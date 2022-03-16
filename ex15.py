dia = int(input("Quantidade de dias que o carro foi alugado: "))
km = float(input("Quantidade de KM percorridos: "))
total = (60 * dia) + (km * 0.15)
print(f"O total a pagar é de R${total}")