from email.errors import InvalidDateDefect


idade = int(input("Idade do atleta: "))
if idade <= 9:
    print("ATLETA MIRIM") 
elif idade > 9 and idade <= 14:
    print("ATLETA INFANTIL")
elif idade > 14 and idade <= 19:
    print("ATLETA JUNIOR")
elif idade > 19 and idade <= 20:
    print("ATLETA SENIOR")
elif idade > 20:
    print("ATLETA MASTER")