primeiro = int(input('termo: '))
razao = int(input('razao: '))
decimo = primeiro +(10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i), end=' > ') 