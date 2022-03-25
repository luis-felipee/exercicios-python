from datetime import date
atual = date.today().year
totMaior = 0
totMenor = 0
for i in range(1, 8):
    ano = int(input(f"Em que ano a {i}° pessoa nasceu: "))
    idade = atual - ano
    if idade >= 21:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print(f"Ao todo tivemos {cont} pessoas maiores de idade")
print(f"Ao todo tivemos {cont2} pessoas menores de idade")
