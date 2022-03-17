salario = float(input("Qual é seu salário: "))
if salario >= 1250:
    novo = salario + ( salario * 10 / 100)
    print(f"O salário com aumento de 10% fica R${novo :.2f}")
else: 
    novo = salario + ( salario * 15 / 100)
    print(f"O salário com aumento de 15% fica R${novo :.2f}")