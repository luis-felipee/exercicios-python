valorCasa = float(input("Valor do imóvel: "))
salario = float(input("Salário do comprador: "))
anos = int(input("Em quantos anos irá pagar: "))

prestacao = int(valorCasa / (anos * 12))
porcentagem = int(salario * 30 / 100)

print(f'30% do salário é igual a: R${porcentagem}')
print(f'Prestação do imóvel: R${prestacao}')
if prestacao <= porcentagem:
    print("Empréstimo aprovado!")
elif prestacao > porcentagem:
    print("Empréstimo negado!")
