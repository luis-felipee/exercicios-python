import math
angulo = int(input("Digite o ângulo que você deseja: "))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
sen = math.sin(math.radians(angulo))

print(f'O valor do {sen :.2f} seno, {cos :.2f} cosseno, {tan :.2f} tangente')
