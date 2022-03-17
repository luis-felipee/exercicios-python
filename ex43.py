from xml.sax.handler import property_interning_dict


altura = float(input("Qual é sua altura: "))
peso = float(input("Qual é seu peso: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu imc de {imc :.2f}, Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print(f"Seu imc de {imc :.2f}, Peso ideal!")
elif imc >= 25 and imc < 30:
    print(f"Seu imc de {imc :.2f}, Sobrepeso")
elif imc >= 30 and imc < 40:
    print(f"Seu imc de {imc :.2f}, Obesidade")
elif imc > 40:
    print(f"Seu imc de {imc :.2f}, Obesidade mórbida")