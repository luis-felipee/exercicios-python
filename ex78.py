valores = []
mai = 0
men = 0
for i in range(0, 5):
    valores.append(int(input(f"Enter a number for the position {i}: ")))
    if i == 0:
        mai = men = valores[i]
    else:
        if valores[i] > mai:
            mai = valores[i]
        if valores[i] < men:
            men = valores[i]
print('-=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}... ', end='')
print()
# print(f'O maior valor digitado foi {max(valores)} nas posição {valores.index(max(valores))}')
# print(f'O menor valor digitado foi {max(valores)} na posição {valores.index(min(valores))}')