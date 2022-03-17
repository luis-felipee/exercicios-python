velocidade = float(input("Velocidade do carro: "))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f"MULTADO! Você excedeu o limite permitido que é de 80Km\h \n você deve pagar uma multa de R${multa :.2f}!")
print("Tenha um bom dia! Dirija com segurança!")