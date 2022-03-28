listagem = ('Lápis', 1.75, 'Notebook', 3200, 'Monitor', 1700, 'Mouse', 160)
print('--' * 20)
print('LISTAGEM DE PREÇOS'.strip())
print('--' * 20)
for pos in range(0, len(listagem)): 
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')