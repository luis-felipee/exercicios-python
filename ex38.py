n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
if n1 > n2:
    print(f'O primeiro valor: {n1}, é maior que {n2}')
elif n2 > n1:
    print(f'O segundo valor: {n2}, é maior que {n1}')
elif n1 == n2:
    print(f'Não existe valor maior, os valores: {n1} e {n2} são iguais')