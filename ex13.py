salario = float(input('Qual é o salário do funcionário? R$'))
bonus = 15 / 100
aumento = salario + (bonus * salario)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, aumento))
