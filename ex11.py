
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
m = largura * altura
print("Sua parede tem dimensão {} x {} e sua área é de {} m²".format(largura, altura, m))
print("Para pintar essa parede, você precisará de {}L de tinta".format(m / 2))