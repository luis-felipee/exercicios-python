numero = int(input("Digite um número: "))
opcao = str(input("[1] para binário, [2] para octal, [3] para hexadecimal: "))

if opcao == '1':
    print(f"O número em binário: {numero:b}")
elif opcao == '2':
    print(f"O número em octal: {numero:o}")
elif opcao == '3':
    print(f"Para hexadecimal {numero:x}")