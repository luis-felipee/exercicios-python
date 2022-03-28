numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    user = int(input("Digite um número entre 1 e 10: "))
    if user < 0 or user > 10:
        print("Tente novamente. ", end='')
        continue
    print(f'Você digitou o número {numeros[user]}')
    break
print("All done!")