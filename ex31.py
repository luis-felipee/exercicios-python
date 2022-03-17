dist = int(input("Qual a distância da sua viagem: "))
if dist <= 200:
    print(f'O preço será {dist * 0.50 :.2f}')
else:
    print(f'O preço será {dist * 0.45 :.2f}')