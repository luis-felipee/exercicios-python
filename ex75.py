tupla = (int(input('insira um número:')), int(input('insira um número:')), int(input('insira um número:')), int(input('insira um número:')))
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 está na  {tupla.index(3)}ª posição')
else:
    print('O  valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')