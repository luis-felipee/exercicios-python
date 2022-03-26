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
