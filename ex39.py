ano = int(input("Ano de nascimento: "))
if ano == 2004:
    print("É HORA DE SE ALISTAR NO SERVIÇO MILITAR!")
elif ano > 2004:
    print(f"FALTAM {ano - 2004} ANO(S) PARA VOCÊ SE ALISTAR!")
elif ano < 2004:
    print(F" JÁ PASSOU {2004 - ano} ANOS PARA O ALISTAMENTO, VOCÊ ESTÁ ATRASADO!")