# n = None
# even = 0
# odd = 0
# while n != 0:
#     try:
#         n =  int(input("Digite um valor: "))
#         if n % 2 == 0:
#             even = even + 1
#         if n % 2 != 0:
#             odd = odd + 1
#     except:
#         print("Você não digitou um número!")
#         continue
# print('Acabou')
# print(f"Even numbers: {even} ")
# print(f"Odd numbers: {odd} ")

g = None
while True:
    try:
        g =  str(input("Qual seu sexo: ")).upper()
        if g == 'M' or g == 'F':
            break
        else:
            print("Digite F para feminino ou M para masculino!")
            continue
    except: 
        print("Digite novamente")
        continue
print("Seu sexo é ", g)
print("All done")