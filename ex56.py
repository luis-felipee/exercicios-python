somaidade = 0
mediaIdade = 0
maioridadeH = 0
nomeVelho = ''
totmulher20 = 0
for i in range(1, 5):
    print(f'--------- {i}ª PESSOA --------')
    nome = str(input(f"Nome da {i}ª pessoa: ")).strip()
    idade = int(input(f"Idade da {i}ª pessoa: "))
    sexo = str(input(f"Sexo da {i}ª pessoa: ")).strip().lower()
    somaidade += idade
    if i == 1 and sexo in 'm':
        maioridadeH = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maioridadeH:
        maioridadeH = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaIdade = somaidade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos')
print(f'O homem mais velho tem {maioridadeH} anos e se chama {nomeVelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')